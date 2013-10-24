import sys
import time
import socket
from netaddr import *
from datetime import datetime
from struct import *

class IPProto(object):
    src = None
    dest = None
    header = 0    
    family = socket.AF_INET
    sock = None
    messageproto = None
    
    def __init__(self, dest, messageproto):
        self.dest = dest
        self.messageproto = messageproto
        self.family = socket.AF_INET6 if self.dest.version == 6 else socket.AF_INET
        self.src = self.detectsrcip()
        
    def detectsrcip(self):
        self.src = IPAddress(socket.getaddrinfo(socket.gethostname(), None, self.family)[0][4][0])
        return self.src
    
    
class ProtoTest(object):
    datetime = None
    protoname = ""
    dest = ""
    port = ""
    ipproto = None
    state = ""
    
    def __init__(self, protoname, prototype, dest, port):
        self.dest = dest
        self.port = port
        self.protoname = protoname
        self.datetime = datetime.now()
        self.ipproto = IPProto(dest, prototype)
        
    @staticmethod
    def gettest(protoname, dest, port):
        testname = protoname.upper()
        return globals()[testname + "Test"](dest, port)
        
    
class TCPTest(ProtoTest):
    header = 0
    
    def __init__(self, dest, port):
        ProtoTest.__init__(self, "tcp", socket.IPPROTO_TCP, dest, port)
        self.test()
    
    def test(self):
        self.state = "close"
        try:
            sock = socket.create_connection((str(self.dest), self.port), 0.2)
            self.state = "open"
        except socket.error:
            self.state = "close"
            pass
        except:
            print("exception:",sys.exc_info()[0], ":", sys.exc_info()[1])
            pass
        
class UDPTest(ProtoTest):
    def __init__(self, dest, port):
        ProtoTest.__init__(self, "udp", socket.IPPROTO_UDP, dest, port)
        self.state = "close"
        

        