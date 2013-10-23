import sys
import utils
from pprint import pprint
from netaddr import *
from host import Host
from port import Port

__author__="godard_b"
__date__ ="$Sep 30, 2013 3:52:38 PM$"

class PortScanner(object):    
    hosts = {}

    def scan(self, hosts, ports = "0-1024"):
        for address in Host.hosts_list(hosts, ports):
            self.hosts[str(address[0])] = Host(address)

if __name__ == "__main__":
    portscanner = PortScanner();
    if len(sys.argv) > 1:
        try:
            cmdParser = utils.CmdParser()
            args = cmdParser.get_args()
            portscanner.scan(args.host, args.port)
        except SystemExit:
            pass
        except:
            # TODO: Debug
            print("Exception : ", sys.exc_info())
            raise
            