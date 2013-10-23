
import sys
import socket
from pprint import pprint
from netaddr import *

__author__  = "ignati_i"
__date__    =   "$Sep 30, 2013 3:53:32 PM$"

class Port(object):
    """ Describe port of host """
    port_number = 0
    hostname = ""
    serv_name = ""
    state = ""
    
    def __init__(self, hostname, port_number):
        self.port_number = port_number
        self.hostname = hostname;
        
        # TODO : add option for timeout
        # TODO : add option for passive scan
        # TODO : add filtered detection
        
        try:
            self.serv_name = socket.getservbyport(port_number)
        except socket.error:
            self.serv_name = "undef"
        
        try:
            #if self.hostname.version == 6:
            #    sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW)
            #else:
            #    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW)
            #packet = TCPPacket(sock, self.hostname, 0)
            #packet.send()
            #if (packet.hasanswer()):
            #    self.state = "open"
            #else:
            #    self.state = "filtered"
            
            sock = socket.create_connection((str(self.hostname), self.port_number), 0.2)
            sock.send(bytes(32))
            if (len(sock.recv(32)) > 0):
                self.state = "open"
            else:
                self.state = "filtered"
            sock.close()
        except:
            self.state = "close"
            
            # TODO: Debug
            print("Exception : ", sys.exc_info())
            raise
        print(self.__str__());
            
    def __str__(self):
        return str(":".join([str(self.port_number), self.state, self.serv_name]))
    
    @staticmethod
    def ports_list(ports):
        ports.strip()
        ports_ranges = ports.split(",")
        for port_range in ports_ranges:
            if port_range.find("-") >= 0:
                rng = port_range.split("-")
                for i in range(int(rng[0]), int(rng[1]) + 1):
                    yield i
            else:
                yield int(port_range)