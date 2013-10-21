
import socket
import re
from pprint import pprint
from netaddr import *
from port import Port

__author__  =   "ignati_i"
__date__    =   "$Sep 30, 2013 3:53:32 PM$"

class Host(object):
    """ Describe scanning host """
    ip_address = ""
    ports_list = []
    ports = {}
    
    def __init__(self, address):
        self.ip_address = address[0]
        self.ports_list = Port.ports_list(address[1])
        
        print("init host : " , self.ip_address, " [ " , self.ports_list, " ] ")
        self.port_scan()
        
    def __str__(self):
        """ Convert host object to string representation """
        
        return str(self.ip_address)

    def port_scan(self):
        """ Scan range of ports """
        
        # TODO : random port choose for scaning
        
        for port in self.ports_list:
            self.ports[port] = Port(self.ip_address, port)
        
        return self.ports
    
    @staticmethod
    def hosts_list(hosts, default_ports = "0-1024"):
        """ Create from string hosts list of addresses """
        hosts = hosts.strip()
        hosts_list = []        
        hosts_ranges = re.findall(r"((?:(?:\([^(),]+\))|(?:[^(),:\-]+)):?(?:(?:\([^()]+\))|(?:[^(),:\-]+))),?", hosts)
        
        for host in hosts_ranges:
            port = default_ports
            
            if host.find("):") >= 0:
                """ IPv6 with port detected """
                host, port = tuple(host.split("):"))
                host = host.replace("(", "").replace(")", "")
                port = port.replace("(", "").replace(")", "")
            elif host.find(":") >= 0:                
                host, port = tuple(host.replace("(", "").replace(")", "").split(":"))
                
            if host.find("/") > 0:
                hosts_list.extend([(ip, port) for ip in IPNetwork(host)])
            elif host.find("-") > 0:
                start_host, end_host = tuple(host.split("-"))
                hosts_list.extend([(ip, port) for ip in list(iter_iprange(start_host, end_host))])
            else:
                hosts_list.append((IPAddress(host), port))
                
        return hosts_list
    
    
    
    
    
        