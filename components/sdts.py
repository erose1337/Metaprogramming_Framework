import pride.components.datatransfer

import epqcrypto.protocol
import epqcrypto.hashing

class Secure_Data_Transfer_Client(pride.components.datatransfer.Data_Transfer_Client):
    
    defaults = {"public_key" : None, "private_key" : None,
                "hash_function" : epqcrypto.hashing.hash_function, "secret_size" : 32}
    
    mutable_defaults = {"secure_connections" : dict}
            
    def _get_connection_arguments(self):
        return self.public_key, self.private_key, self.hash_function, self.secret_size
    connection_arguments = property(_get_connection_arguments)
    
    def __init__(self, *args, **kwargs):
        super(Secure_Data_Transfer_Client, self).__init__(*args, **kwargs)
        if not (self.public_key and self.private_key):
            self.alert("Keypair not supplied;")
            if pride.components.shell.get_permission("{}: Generate new keypair now?: ".format(self.reference)):
                self.public_key, self.private_key = epqcrypto.protocol.keyexchange.generate_keypair()
            else:
                raise ValueError("Public/Private keypair is required to continue")
        
    def connect(self, identity, peer_public_key):        
        try:
            connection = self.secure_connections[identity]
        except KeyError:
            connection = self.new_connection(identity)        
        self.send_to(identity, connection.connect(peer_public_key))

    def send_to(self, identity, data):        
        if identity:            
            if identity not in self.secure_connections:
                raise ValueError("Not connected to '{}'".format(identity))
            connection = self.secure_connections[identity]
            if connection.connection_confirmed:                
                data = connection.send(data)                   
        super(Secure_Data_Transfer_Client, self).send_to(identity, data)
        
    def receive(self, messages):
        for sender, data in messages:            
            try:
                connection = self.secure_connections[sender]
            except KeyError:
                connection = self.new_connection(sender)       
                response = connection.accept(data)
            else:
                if connection.stage == "connecting":
                    response = connection.initiator_confirm_connection(data)
                    connection.connection_confirmed = False
                    self.send_to(sender, response)
                    connection.connection_confirmed = True
                    response = ''
                elif connection.stage == "accepted:confirming":                    
                    response = connection.responder_confirm_connection(data)
                elif connection.connection_confirmed:                    
                    data = connection.receive(data)
                    response = self.handle_data(sender, data)
            if response:
                self.send_to(sender, response)
                
    def handle_data(self, sender, data):
        self.alert("{}: {}".format(sender, data))
                    
    def new_connection(self, identity):
        assert identity not in self.secure_connections
        connection = self.create(epqcrypto.protocol.Secure_Connection, *self.connection_arguments)        
        self.secure_connections[identity] = connection
        return connection
        
    @classmethod
    def unit_test(cls):
        client1 = cls(username="unit_test1")
        client2 = cls(username="unit_test2")
        client1.connect(client2.username, client2.public_key)
        
        
        