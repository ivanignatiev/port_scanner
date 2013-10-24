import sys
import socket
from pprint import pprint
from netaddr import *
from prototests import *

class Port(object):
    """ Describe port of host """
    port_number = 0
    hostname = ""
    serv_name = ""
    tests = []
    
    def __init__(self, hostname, port_number):
        self.tests = []
        self.port_number = port_number
        self.hostname = hostname;
        self.test()
            
    def __str__(self):
        info = ":".join([str(self.port_number), self.serv_name])
        for test in self.tests:
            info = info + ":" + test.protoname + ":" + test.state
        return info
    
    def testProto(self, protoname):
        try:
            test = ProtoTest.gettest(protoname, self.hostname, self.port_number)
            self.tests.append(test)
        except:    
            #print("exception:",sys.exc_info()[0], ":", sys.exc_info()[1])
            pass
        return None
        
    def test(self):
        self.testProto("tcp")
        self.testProto("udp")
        try:
            self.serv_name = socket.getservbyport(self.port_number)
            self.testProto(self.serv_name)
        except socket.error:
            self.serv_name = "undef"
            pass
        
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