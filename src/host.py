import socket
import re
import random
from pprint import pprint
from netaddr import *
from port import Port

class Host(object):
    """ Describe scanning host """
    address = ()
    ports = {}
    
    def __init__(self, address):
        self.address = address
        print("scan:" , str(self.address[0]))
        self.port_scan()
        
    def __str__(self):
        """ Convert host object to string representation """
        return str(self.address)

    def port_scan(self):
        """ Scan range of ports """
        scan_ports = list(Port.ports_list(self.address[1]))
        random.shuffle(scan_ports)
        for port in scan_ports:
            self.ports[port] = Port(self.address[0], port)
            print(self.ports[port])
        return self.ports
    
    @staticmethod
    def resolv_dns(host):
        resolved_host = socket.getaddrinfo(host, None, socket.AF_UNSPEC)[0][4][0]
        if not host == resolved_host:
            print(host, ":resolved_like:", resolved_host)
        return resolved_host
    
    @staticmethod
    def hosts_list(hosts, default_ports = "0-1024"):
        """ Create from string hosts list of addresses """
        hosts = hosts.strip()
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
                for ip in IPNetwork(Host.resolv_dns(host)):
                    yield (ip, port)
            elif host.find("-") > 0:
                start_host, end_host = tuple(host.split("-"))
                for ip in iter_iprange(Host.resolv_dns(start_host), Host.resolv_dns(end_host)):
                    yield (ip, port)
            else:
                yield (IPAddress(Host.resolv_dns(host)), port)
    
    
    
    
    
        