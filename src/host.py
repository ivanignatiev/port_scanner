
import socket
from port import Port

__author__  =   "ignati_i"
__date__    =   "$Sep 30, 2013 3:53:32 PM$"

class Host(object):
    """ Describe scanning host """
    hostname = 0
    ports_to_scan = []
    ports = {}
    
    def __init__(self, hostname, ports_to_scan):
        self.hostname = hostname
        self.ports_to_scan = Port.ports_list(ports_to_scan)
        
        print("init host : " , self.hostname, " [ " , self.ports_to_scan, " ] ")
        self.port_scan()
        
    def __str__(self):
        """ Convert host object to string representation """
        
        return str(self.host)

    def port_scan(self):
        """ Scan range of ports """
        
        for port in self.ports_to_scan:
            self.ports[port] = Port(self.hostname, port)
        
        return self.ports
    
    @staticmethod
    def host_ip(host):
        for host in socket.getaddrinfo(host, 0):
            if host[0] == socket.AF_INET or host[0] == socket.AF_INET6:
                return host[4][0]
        raise NameError("Can't resolve host : " + host)
        
    
    
    @staticmethod
    def hosts_list(hosts):
        """ Create from string hosts list of addresses """
        hosts = hosts.strip()
        hosts_list = []
        hosts_ranges = hosts.split(",")
        for host in hosts_ranges:
            if host.find("-") >= 0:
                rng = host.split("-")
                start_host_addr = Host.host_ip(rng[0])
                end_host_addr   = Host.host_ip(rng[1])
                hosts_list.append(Host.host_ip(start_host_addr))
                hosts_list.append(Host.host_ip(end_host_addr))
                # hosts_list = hosts_list + list(iter_iprange(start_host_addr, end_host_addr))
                # TODO : enable netaddr lib
            else:
                try:
                    hosts_list.append(Host.host_ip(host))
                except:
                    print("unresolved host : " , host)
        return hosts_list
        