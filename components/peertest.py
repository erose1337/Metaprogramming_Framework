import pride.components.base.Base

class Peer(pride.components.base.Base):
    
    def __init__(self, *args, **kwargs):
        super(Peer, self).__init__(*args, **kwargs)
        self.beacon = self.create("pride.components.network.Multicast_Beacon")
        self.receiver = self.create("pride.components.network.Multicast_Receiver")
        