""" pride.rpc - Remote Procedure Call portal built on top of pride.networkssl ssl sockets

    SECURITY NOTE: the current implementation uses pickle for serialization 
                   and is to be considered completely insecure """
import struct
import traceback
import json
import pickle

import pride
import pride.base
import pride.network
import pride.networkssl
import pride.authentication
import pride.persistence
import pride.decorators
objects = pride.objects

default_serializer = pickle
_old_data, _hosts = {}, {}

def packetize_send(send):
    """ Decorator that transforms a tcp stream into packets. Requires the use
        of the packetize_recv decorator on the recv end. """
    def _send(self, data):
        return send(self, str(len(data)) + ' ' + data)   
    return _send
    
def packetize_recv(recv):
    """ Decorator that breaks a tcp stream into packets based on packet sizes,
        as supplied by the corresponding packetize_send decorator. In the event
        less then an entire packet is received, the received data is stored 
        until the remainder is received.
        
        The recv method decorated by this function will return a list of
        packets received or an empty list if no complete packets have been
        received. """        
    def _recv(self, buffer_size=0):
        try:
            data = _old_data[self] + recv(self, buffer_size)
        except KeyError:
            data = recv(self, buffer_size)            
        _old_data[self] = ''
        packets = []
        while data:
            try:
                packet_size, data = data.split(' ', 1)
            except ValueError:
                _old_data[self] = data
                break
            packet_size = int(packet_size)
            packets.append(data[:packet_size])
            data = data[packet_size:]   
        return packets    
    return _recv
   
        
class Session(pride.base.Base):
    """ Maintains session id information and prepares outgoing requests """
    defaults = {"id" : '0', "host_info" : tuple(), 
                "requester_type" : "pride.rpc.Rpc_Client"}
    
    def _get_id(self):
        return self._id
    def _set_id(self, value):
        self._id = value
        self.id_size = struct.pack('l', len(value))
    id = property(_get_id, _set_id)
    
    def _get_context(self):
        return self.id, self.host_info
    context = property(_get_context)
    
    def __init__(self, session_id, host_info, **kwargs):
        self._callbacks = []
        super(Session, self).__init__(**kwargs)
        self.id = session_id
        self.host_info = host_info
            
    def execute(self, instruction, callback):
        """ Prepare instruction as a request to be sent by an Rpc_Client. A 
            request consists of session id information (size and id#), 
            followed by the information from the supplied instruction. No
            information regarding the callback is included in the request. """
        _call = component, method = instruction.component_name, instruction.method
        request = ' '.join((self.id_size + self.id, component, method, 
                            default_serializer.dumps((instruction.args, 
                                                      instruction.kwargs))))
        try:
            host = _hosts[self.host_info]
        except KeyError:
            host = _hosts[self.host_info] = self.create(self.requester_type,
                                                        host_info=self.host_info)                                                        
        if host.bypass_network_stack and host._endpoint_instance_name:
            self._callbacks.insert(0, (_call, callback))
        else:
            self._callbacks.append((_call, callback))
      #  self.alert("Storing callback: {}. callbacks: {}".format(callback, self._callbacks), level=0)  
        host.make_request(request, self.instance_name)
       
    def __next__(self): # python 3
        return self._callbacks.pop(0)
      
    def next(self): # python 2   
        return self._callbacks.pop(0)
        
            
class Packet_Client(pride.networkssl.SSL_Client):
    """ An SSL_Client that uses packetized send and recv (client side) """        
    defaults = {"_old_data" : bytes()}
    
    @packetize_send
    def send(self, data):
        return super(Packet_Client, self).send(data)
    
    @packetize_recv
    def recv(self, buffer_size=0):
        return super(Packet_Client, self).recv(buffer_size)      
        
        
class Packet_Socket(pride.networkssl.SSL_Socket):
    """ An SSL_Socket that uses packetized send and recv (server side) """        
    defaults = {"_old_data" : bytes()}
    
    @packetize_send
    def send(self, data):
        return super(Packet_Socket, self).send(data)
    
    @packetize_recv
    def recv(self, buffer_size=0):        
        return super(Packet_Socket, self).recv(buffer_size)
                       
                        
class Rpc_Server(pride.networkssl.SSL_Server):
    """ Creates Rpc_Sockets for handling rpc requests. By default, this
        server runs on the localhost only, meaning it is not accessible 
        from the network. """
    defaults = {"port" : 40022,
                "interface" : "localhost",
                "Tcp_Socket_type" : "pride.rpc.Rpc_Socket"}
    
    
class Rpc_Client(Packet_Client):
    """ Client socket for making rpc requests using packetized tcp stream. """  
    verbosity = {"delayed_request_sent" : "vv", "request_delayed" : "vv",
                 "request_sent" : "vv", "unresolved_callback" : 0, "handle_exception" : 0}
                 
    def __init__(self, **kwargs):
        self._requests, self._callbacks = [], []
        super(Rpc_Client, self).__init__(**kwargs)
        
    def on_ssl_authentication(self):
        count = 1
        length = len(self._requests)
        for request, callback in self._requests:
            self.alert("Making delayed request {}/{}: {}".format(count, length, request)[:128], 
                       level=self.verbosity["delayed_request_sent"])
            self._callbacks.append(callback)  
            self.send(request)
            
    def make_request(self, request, callback_owner):
        """ Send request to remote host and queue callback_owner for callback """
        if not self.ssl_authenticated:
            self.alert("Delaying request until authenticated: {}".format(request)[:128], 
                       level=self.verbosity["request_delayed"])
            self._requests.append((request, callback_owner))
        else:    
            self.alert("Making request for {}".format(callback_owner), level=self.verbosity["request_sent"])
            self._callbacks.append(callback_owner)
            self.send(request)            
        
    def recv(self, packet_count=0):
        for response in super(Rpc_Client, self).recv():
         #   print "Deserealizing: ", len(response), response
            _response = self.deserealize(response)
            callback_owner = self._callbacks.pop(0)
            try:
                _call, callback = next(pride.objects[callback_owner])
            except KeyError:
                self.alert("Could not resolve callback_owner '{}' for {} {}",
                           (callback_owner, "callback with arguments {}",
                            _response), level=self.verbosity["unresolved_callback"])
            else:
                if isinstance(_response, BaseException):
                    self.handle_exception(_call, callback, _response)
                elif callback is not None:
                    callback(_response)                                
                                                
    def handle_exception(self, _call, callback, response):
        self.alert("\n    Remote Traceback: Exception calling {}: {}: {}\n    Unable to proceed with callback {}",
                   ('.'.join(_call), response.__class__.__name__, 
                    getattr(response, "traceback", response), callback), 
                   level=self.verbosity["handle_exception"])
        if (isinstance(response, SystemExit) or 
            isinstance(response, KeyboardInterrupt)):
            print "Reraising exception", type(response)()
            raise type(response)()            
            
    def deserealize(self, response):
        return default_serializer.loads(response)
        
        
class Rpc_Socket(Packet_Socket):
    """ Packetized tcp socket for handling and performing rpc requests """
    
    verbosity = {"request_exception" : 'v', "request_denied" : 'v',
                 "request_result" : "vvv"}
                 
    def recv(self, packet_count=0):
        peername = self.peername
        for packet in super(Rpc_Socket, self).recv():
            session_id_size = struct.unpack('l', packet[:4])[0]
            end_session_id = 4 + session_id_size
            
            session_id = packet[4:end_session_id]
            (component_name, method, 
             serialized_arguments) = packet[end_session_id + 1:].split(' ', 2)

            try:
                instance = pride.objects[component_name]
            except KeyError as result:
                pass
            else:
                permission = False
                if session_id == '0' and method in ("register", "login"):
                    permission = True        
                    
                if not hasattr(instance, "validate"):
                    result = pride.authentication.UnauthorizedError()
                elif permission or instance.validate(session_id, 
                                                     peername, method):
                    try:
                        args, kwargs = self.deserealize(serialized_arguments)
                        result = getattr(instance, method)(*args, **kwargs)
                    except BaseException as result:
                        stack_trace = traceback.format_exc()
                        self.alert("Exception processing request {}.{}: \n{}",
                                   [component_name, method, stack_trace],
                                   level=self.verbosty["request_exception"])
                        if isinstance(result, SystemExit):
                            raise                                   
                        result.traceback = stack_trace
                else:
                    self.alert("Denying unauthorized request: {}",
                               (packet, ), level=self.verbosity["request_denied"])
                    result = pride.authentication.UnauthorizedError()
            self.alert("Sending result of {}.{}: {}",
                       (component_name, method, result), level=self.verbosity["request_result"])
            self.send(self.serealize(result))
            
    def deserealize(self, serialized_arguments):
        return default_serializer.loads(serialized_arguments)
        
    def serealize(self, result):
        return default_serializer.dumps(result)
