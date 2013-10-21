import sys
import utils
from pprint import pprint
from netaddr import *
from host import Host
from port import Port

__author__="godard_b"
__date__ ="$Sep 30, 2013 3:52:38 PM$"

if __name__ == "__main__":
    try:
        cmdParser = utils.CmdParser()
        args = cmdParser.get_args()
    
        hosts = {}
        
        for address in Host.hosts_list(args.host, args.port):
            hosts[address[0]] = Host(address)
        
    except:
        print("Exception : ", sys.exc_info())
        raise
