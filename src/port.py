
import socket

__author__  = "ignati_i"
__date__    =   "$Sep 30, 2013 3:53:32 PM$"

class Port(object):
    """ Describe port of host """
    port_number = 0
    hostname = ""
    serv_name = ""
    connection = None
    
    def __init__(self, hostname, port_number):
        self.port_number = port_number
        self.hostname = hostname;
        
        # TODO : add option for timeout
        
        try:
            self.serv_name = socket.getservbyport(port_number)
        except socket.error:
            self.serv_name = "undef"
        
        try:
            self.connection = socket.create_connection((self.hostname, self.port_number), 0.5)
            print("connection open : " , port_number, "/",  self.serv_name)
            self.connection.close()
        except:
            self.connection = None
            print("connection close : " , port_number, "/",  self.serv_name)
        
    def __str__(self):
        return str(self.port_number)
    
    @staticmethod
    def ports_list(ports):
        ports.strip()
        ports_list = []
        ports_ranges = ports.split(",")
        for port_range in ports_ranges:
            if port_range.find("-") >= 0:
                rng = port_range.split("-")
                ports_list = ports_list + list(range(int(rng[0]), int(rng[1]) + 1))
            else:
                ports_list.append(int(port_range))
        return ports_list
    