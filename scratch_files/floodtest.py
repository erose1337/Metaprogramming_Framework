import pride.components.network
import pride.components.scheduler
import pride.components.datastructures
import pride.functions.utilities
print_in_place = pride.functions.utilities.print_in_place

class Connection_Tester(pride.components.network.Tcp_Client):
    
    def on_connect(self):
        self.delete()
        

class Connection_Flood(pride.components.scheduler.Process):
            
    defaults = {"target" : None, "priority" : .01, "swarm_size" : 25}
    required_arguments = ("target", )
    mutable_defaults = {"latency" : pride.components.datastructures.Latency}
    
    def run(self):
        target = self.target
        latency = self.latency
        latency.mark()
        print_in_place(str(latency.average))
        for x in xrange(self.swarm_size):
            self.create(Connection_Tester, host_info=target)
            
if __name__ == "__main__":
    Connection_Flood(target=("192.168.1.254", 80))