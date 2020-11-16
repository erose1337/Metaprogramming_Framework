""" pride.components.rpc - Remote Procedure Call portal built on top of pride.components.networkssl ssl sockets. """
import struct
import traceback
import itertools
import time
import functools
from os import path
import socket
import traceback

import pride
import pride.components.base
import pride.components.scheduler
import pride.components.networkssl
import pride.components.network
import pride.functions.decorators
from pride.errors import UnauthorizedError

DEFAULT_SERIALIZER = pride.components.network.DEFAULT_SERIALIZER

NO_ERROR = 0
UNAUTHORIZED_ERROR = 1
CODE_ERROR = 2
GENERIC_ERROR = 3

def Result(error_code, message=''):
    return (error_code, message)


@pride.functions.decorators.required_arguments(no_args=True)
def remote_procedure_call(callback_name='', callback=None):
    def decorate(function):
        call_name = function.__name__

        @functools.wraps(function)
        def _make_rpc(self, *args, **kwargs):
            if callback_name:
                _callback = getattr(self, callback_name)
            else:
                _callback = callback or None

            instruction = pride.Instruction(self.target_service, call_name, *args, **kwargs)
            if not getattr(self, "logged_in", True) and call_name not in ("register", "login", "login_stage_two"):
                self.handle_not_logged_in(instruction, _callback)
            else:
                self.alert("Making request '{}.{}'".format(self.target_service, call_name),
                           level=self.verbosity.get(call_name, 'v'))
                self.session.execute(instruction, _callback)
        return _make_rpc
    return decorate


class Session(pride.components.base.Base):
    """ Maintains session id information and prepares outgoing requests """
    defaults = {"requester_type" : "pride.components.rpc.Rpc_Client_Socket",
                "session_id" : None, "host_info" : None}

    predefaults = {"_id" : None}
    mutable_defaults = {"_callbacks" : list}

    required_attributes = ("session_id", "host_info")

    def _get_id(self):
        return self._id
    def _set_id(self, value):
        self._id = value
        self.id_size = struct.pack('l', len(value))
    id = property(_get_id, _set_id)

    def _get_context(self):
        return self.id, self.host_info
    context = property(_get_context)

    def execute(self, instruction, callback):
        """ Prepare instruction as a request to be sent by an Rpc_Client_Socket. A
            request consists of session id information (size and id#),
            followed by the information from the supplied instruction. No
            information regarding the callback is included in the request. """
        _call = component, method = instruction.component_name, instruction.method
        request = DEFAULT_SERIALIZER.dumps(self.id, component, method,
                                           DEFAULT_SERIALIZER.dumps((instruction.args, instruction.kwargs)))
        host = pride.objects["/Program/Rpc_Connection_Manager"].get_host(self.host_info)
        self._callbacks.append((_call, callback))
        host.make_request(request, self.reference)

    def next_callback(self):
        return self._callbacks.pop(0)


class Packet_Client(pride.components.networkssl.SSL_Client):
    """ An SSL_Client that uses packetized send and recv (client side) """
    defaults = {"_old_data" : bytes()}

    def send(self, data):
        return super(Packet_Client, self).send(str(len(data)) + ' ' + data)

    def recv(self, buffer_size=0):
        try:
            data = self._old_data + super(Packet_Client, self).recv(buffer_size)
        except socket.error as error: # which error did we really intend to catch here?
            if error.errno == pride.components.network.CONNECTION_CLOSED:
                raise
            data = self._old_data

        self._old_data = bytearray()
        packets = []
        while data:
            try:
                packet_size, data = data.split(' ', 1)
            except ValueError:
                self._old_data = data
                break

            packet_size = int(packet_size)
            if len(data) < packet_size:
                self._old_data = bytes(packet_size) + ' ' + data
                break

            packets.append(data[:packet_size])
            data = data[packet_size:]
        return packets


class Packet_Socket(pride.components.networkssl.SSL_Socket):
    """ An SSL_Socket that uses packetized send and recv (server side) """
    defaults = {"_old_data" : bytes()}

    def send(self, data):
        return super(Packet_Socket, self).send(str(len(data)) + ' ' + data)

    def recv(self, buffer_size=0):
        try:
            data = self._old_data + super(Packet_Socket, self).recv(buffer_size)
        except socket.error as error: # which error did we really intend to catch here?
            if error.errno == pride.components.network.CONNECTION_CLOSED:
                raise
            data = self._old_data

        self._old_data = bytearray()
        packets = []
        while data:
            try:
                packet_size, data = data.split(' ', 1)
            except ValueError:
                self._old_data = data
                break

            packet_size = int(packet_size)
            if len(data) < packet_size:
                self._old_data = bytes(packet_size) + ' ' + data
                break

            packets.append(data[:packet_size])
            data = data[packet_size:]
        return packets


class Rpc_Connection_Manager(pride.components.base.Base):
    """ Creates Rpc_Client_Sockets for making rpc requests. Used to facilitate the
        the usage of a single connection for arbitrary requests to the host. """
    defaults = {"requester_type" : "pride.components.rpc.Rpc_Client_Socket"}
    mutable_defaults = {"hosts" : dict}

    def get_host(self, host_info):
        try:
            return self.hosts[host_info]
        except KeyError:
            if host_info in self.hosts:
                raise
            host = self.hosts[host_info] = self.create(self.requester_type, host_info=host_info)
            return host

    def add(self, _object):
        self.hosts[_object.host_info] = _object
        super(Rpc_Connection_Manager, self).add(_object)

    def remove(self, _object):
        super(Rpc_Connection_Manager, self).remove(_object)
        del self.hosts[_object.host_info]

    def __getstate__(self):
        attributes = super(Rpc_Connection_Manager, self).__getstate__()
        attributes["hosts"] = {}
        return attributes


class Rpc_Server(pride.components.networkssl.SSL_Server):
    """ Creates Rpc_Sockets for handling rpc requests. By default, this
        server runs on the localhost only, meaning it is not accessible
        from the network. """
    defaults = {"port" : 40022, "interface" : "localhost",
                "Tcp_Socket_type" : "pride.components.rpc.Rpc_Socket"}


class Rpc_Client_Socket(Packet_Client):
    """ Client socket for making rpc requests using packetized tcp stream. """
    verbosity = {"delayed_request_sent" : "vvv", "request_delayed" : "vvv",
                 "request_sent" : "vvv", "unresolved_callback" : 0,

                 "unauthorized_error" : 0, "code_error" : 0,
                 "generic_error" : 0, "invalid_error_code" : 0}

    mutable_defaults = {"_requests" : list, "_callbacks" : list}

    def on_ssl_authentication(self):
        super(Rpc_Client_Socket, self).on_ssl_authentication()
        count = 1
        length = len(self._requests)
        for request, callback in self._requests:
            self.alert("Making delayed request {}/{}: {}".format(count, length, request)[:128],
                       level=self.verbosity["delayed_request_sent"])
            self._callbacks.append(callback)
            self.send(request)
            count += 1

    def make_request(self, request, callback_owner):
        """ Send request to remote host and queue callback_owner for callback """
        if not self.connected:
            self.alert("Delaying request until authenticated: {}".format(request)[:128],
                       level=self.verbosity["request_delayed"])
            self._requests.append((request, callback_owner))
        else:
            self.alert("Making request for {}".format(callback_owner), level=self.verbosity["request_sent"])
            self._callbacks.append(callback_owner)
            self.send(request)

    def recv(self, packet_count=0):
        for response in super(Rpc_Client_Socket, self).recv():
            rpc_code, _response = self.deserialize(bytes(response))
            callback_owner = self._callbacks.pop(0)
            try:
                _call, callback = pride.objects[callback_owner].next_callback()
            except KeyError:
                message = "Could not resolve callback_owner '{}'"
                self.alert(message.format(callback_owner),
                           level=self.verbosity["unresolved_callback"])
            if rpc_code == NO_ERROR:
                if callback is not None:
                    callback(_response)
            else:
                if rpc_code == UNAUTHORIZED_ERROR:
                    message = self.format_error("Unauthorized Error",
                                                (callback_owner, _call))
                    self.alert(message,
                               level=self.verbosity["unauthorized_error"])
                elif rpc_code == CODE_ERROR:
                    extra = "\nRemote Traceback:\n{}".format(_response)
                    message = self.format_error("Code Error",
                                                (callback_owner, _call),
                                                extra)
                    self.alert(message,
                               level=self.verbosity["code_error"])
                elif rpc_code == GENERIC_ERROR:
                    message = self.format_error("Generic Error",
                                                (callback_owner, _call))
                    self.alert(message,
                               level=self.verbosity["generic_error"])
                else:
                    message = self.format_error("Invalid Error Code",
                                                (callback_owner, _call),
                          "\nReceived invalid error code '{}'".format(rpc_code))
                    self.alert(message,
                               level=self.verbosity["invalid_error_code"])

    def format_error(self, error, caller_info, extra=''):
        client_name, server_info = caller_info
        service_name, procedure_name = server_info
        error_message = error + '\n'
        length = min(79, len(error) + len(self.reference) + 1)
        error_message += ('-' * length) + '\n'
        error_message += "- returned by: "
        error_message += "`{}.{}`".format(service_name, procedure_name)
        error_message += "\n- requested by `{}`".format(client_name)
        error_message += extra
        return error_message



class Rpc_Socket(Packet_Socket):
    """ Packetized tcp socket for receiving and delegating rpc requests """

    defaults = {"idle_after" : 600,
                "production_mode" : "debug"}
                 # this default will provide an adversary with tracebacks
                 # but defaulting to "production" rather than debug seems wrong
    verbosity = {"request_exception" : 'v', "request_result" : "vvv"}
    allowed_values = {"production_mode" : ("debug", "production")}

    def __init__(self, **kwargs):
        super(Rpc_Socket, self).__init__(**kwargs)
        self.rpc_workers = itertools.cycle(objects["/Program"].objects["Rpc_Worker"])

    def on_ssl_authentication(self):
        if self.idle_after:
            self._idle_timer = time.time()
            pride.Instruction(self.reference, "check_idle").execute(priority=self.idle_after)
        return super(Rpc_Socket, self).on_ssl_authentication()

    def check_idle(self):
        if time.time() - self._idle_timer >= self.idle_after:
            self.delete()
        else:
            pride.Instruction(self.reference, "check_idle").execute(priority=self.idle_after)

    def recv(self, packet_count=0):
        peername = self.peername
        assert self.ssl_authenticated
        for (session_id, component_name, method,
             serialized_arguments) in (self.deserialize(bytes(packet)) for
                                       packet in super(Rpc_Socket, self).recv()):
            worker = next(self.rpc_workers)
            try:
                output = worker.handle_request(peername, session_id,
                                               component_name, method,
                                               serialized_arguments)
            except BaseException as result:
                if ((isinstance(result, KeyError) and component_name not in pride.objects) or
                    (isinstance(result, AttributeError) and not hasattr(objects[component_name], "validate")) or
                    isinstance(result, UnauthorizedError)):
                    result = Result(UNAUTHORIZED_ERROR)

                else:
                    assert not isinstance(result, UnauthorizedError)
                    assert not isinstance(result, SystemExit)
                    stack_trace = traceback.format_exc()
                    self.alert("Exception processing request {}.{}: \n{}".format(component_name,
                                                                                 method, stack_trace),
                               level=self.verbosity["request_exception"])

                    if self.production_mode == "debug":
                        stack_trace = traceback.format_exc()
                        result = Result(CODE_ERROR, stack_trace)
                    else:
                        result = Result(GENERIC_ERROR)
            else:
                result = Result(NO_ERROR, output)
                self.alert("Sending result of {}.{}: {}".format(component_name, method, result),
                           level=self.verbosity["request_result"])
            self.send(self.serialize(result))

    def delete(self):
        pride.Instruction.purge(self.reference)
        super(Rpc_Socket, self).delete()


class Rpc_Worker(pride.components.base.Base):
    """ Performs remote procedure call requests """
    defaults = {"serializer" : DEFAULT_SERIALIZER}
    verbosity = {"request_result" : "vvv"}

    def handle_request(self, peername, session_id, component_name, method,
                       serialized_arguments):
        instance = pride.objects[component_name]
        if not instance.validate(session_id, peername, method):
            raise UnauthorizedError()
        else:
            args, kwargs = self.deserialize(serialized_arguments)
            return instance.execute_remote_procedure_call(session_id, peername, method, args, kwargs)

    def deserialize(self, serialized_data):
        return self.serializer.loads(serialized_data)

    def serialize(self, data):
        return self.serializer.dumps(data)

    def __getstate__(self):
        state = super(Rpc_Worker, self).__getstate__()
        state["serializer"] = state["serializer"].__name__
        return state

    def on_load(self, state):
        super(Rpc_Worker, self).on_load(state)
        if state["serializer"] == "Serializer":
            self.serializer = DEFAULT_SERIALIZER
        else:
            raise ValueError("Unsupported serializer '{}'".format(state["serializer"]))


class RPC_Service(pride.components.base.Base):

    defaults = {"database_type" : "pride.components.database.Database",
                "database_name" : '',
                "validation_failure_string" :\
                   ".validate: Authorization Failure:\n" +
                   "    ip blacklisted: {}    ip whitelisted: {}\n" +
                   "    session exists: {}    method name:    {}\n" +
                   "    method available remotely: {}\n" +
                   "    login enabled: {}    registration enabled: {}\n"}
    mutable_defaults = {"_rate" : dict, "ip_whitelist" : list, "ip_blacklist" : list,
                        "session_id" : dict}
    predefaults = {"current_session" : ('', None)}

    verbosity = {"validate_failure" : 0, "validate_success" : 0}

    schema = {}
    databse_flags = {}
    remotely_available_procedures = tuple()
    rate_limit = {}
    inherited_attributes = {"schema" : dict, "database_flags" : dict,
                            "remotely_available_procedures" : tuple, "rate_limit" : dict}

    def __init__(self, **kwargs):
        super(RPC_Service, self).__init__(**kwargs)
        self._load_database()

    def _load_database(self):
        if not self.database_name:
            _reference = '_'.join(name for name in self.reference.split("/") if name)
            name = self.database_name = path.join(pride.site_config.DATABASE_DIRECTORY,
                                                     "{}.db".format(_reference))
        else:
            name = self.database_name
        self.database = self.create(self.database_type, database_name=name,
                                    schema=self.schema,
                                    **self.database_flags)

    def validate(self, session_id, peername, method_name):
        """ Determines whether or not the peer with the supplied
            session id is allowed to call the requested method.

            Sets current_session attribute to (session_id, peername) if validation
            is successful. """
        if ((method_name not in self.remotely_available_procedures) or
            (peername[0] in self.ip_blacklist) or
            (peername[0] not in self.ip_whitelist and self.ip_whitelist)):

            self.alert(self.validation_failure_string.format(peername[0] in self.ip_blacklist,
                                                             peername[0] in self.ip_whitelist,
                                                             method_name,
                                                             method_name in self.remotely_available_procedures),
                       level=self.verbosity["validate_failure"])
            return False

        if self.rate_limit and method_name in self.rate_limit:
            _new_connection = False
            try:
                self._rate[session_id][method_name].mark()
            except KeyError:
                latency = pride.components.datastructures.Latency("{}_{}".format(session_id, method_name))
                try:
                    self._rate[session_id][method_name] = latency
                except KeyError:
                    self._rate[session_id] = {method_name : latency}
                    _new_connection = True
            if not _new_connection:
                current_rate = self._rate[session_id][method_name].last_measurement
                if current_rate < self.rate_limit[method_name]:
                    message = "Rate of {} calls exceeded 1/{}s ({}); Denying request".format(method_name,
                                                                                             self.rate_limit[method_name],
                                                                                             current_rate)
                    self.alert(message, level=self.verbosity["validate_failure"])
                    return False

        self.alert("Authorizing: {} for {}".format(peername, method_name),
                  level=self.verbosity["validate_success"])
        return True

    def execute_remote_procedure_call(self, session_id, peername, method_name, args, kwargs):
        with pride.functions.contextmanagers.backup(self, "current_session"):
            self.current_session = (session_id, peername)
            return getattr(self, method_name)(*args, **kwargs)

    def __getstate__(self):
        state = super(RPC_Service, self).__getstate__()
        del state["database"]
        return state

    def on_load(self, attributes):
        super(RPC_Service, self).on_load(attributes)
        self._load_database()


class RPC_Client(pride.components.base.Base):

    defaults = {"target_service" : "/Program/RPC_Service", "ip" : "localhost", "port" : 40022}
    mutable_defaults = {"_delayed_requests" : list}
    predefaults = {"bypass_network_stack" : True}
    verbosity = {"delayed_request_sent" : "vv"}

    def _get_host_info(self):
        return (self.ip, self.port)
    def _set_host_info(self, value):
        self.ip, self.port = value
    host_info = property(_get_host_info, _set_host_info)

    def __init__(self, **kwargs):
        super(RPC_Client, self).__init__(**kwargs)
        self.session = self.create("pride.components.rpc.Session", session_id='0', host_info=self.host_info)
