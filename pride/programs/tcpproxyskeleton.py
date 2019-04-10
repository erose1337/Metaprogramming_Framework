import pride.components.network

class Client_Socket(pride.components.network.Tcp_Client):

    defaults = {"ip" : '', "port" : 21} # pass ip to constructor when creating a Client_Socket

    def on_connect(self):
        super(Client_Socket, self).on_connect()
        # insert stuff to do when connection to server succeeds here

    def recv(self, buffer_size=0):
        super(Client_Socket, self).recv(buffer_size)
        # insert stuff to do when data is received here
        # use self.send(...) to send data to the server


class Server_Socket(pride.components.Tcp_Socket):

    def on_connect(self):
        super(Server_Socket, self).on_connect()
        # insert stuff to do when a client connects to this server here

    def recv(self, buffer_size):
        super(Server_Socket, self).recv(buffer_size)
        # insert stuff to do when this server socket receives data from a client
        # use self.send(...) to send data to the client


class _Server(pride.components.network.Server):

    defaults = {"port" : 4000, "Tcp_Socket_type" : Server_Socket}

if __name__ == "__main__":
    _server = pride.objects["/Python"].create(_Server)
    _client = pride.objects["/Python"].create(Client_Socket, ip=insert IP here) # IP is of the form "w.x.y.z"
