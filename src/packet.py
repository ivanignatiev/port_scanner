
import socket

class IPPacket(object):

class TCPPacket(IPPacket):
    socket = None
    packet = 0
    host = ""
    
    def __init_(self, sock, host, packet):
        self.packet = packet
        self.socket = sock
        self.host = host
        
    def send(self):
        self.socket.sendto(self.packet, (str(self.host), 0))
        
    def hasanswer(self):
        self.socket.recvfrom(32, (self.host, 0))
        # if ICMP recv Code == 13 - filtered
        # if no answer - filtered
        # return false
        
        # else
        return true
    
        
class UDPPacket(IPPacket):
    