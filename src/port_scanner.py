import sys
import utils
from host import Host

__author__="godard_b"
__date__ ="$Sep 30, 2013 3:52:38 PM$"

if __name__ == "__main__":
    cmdParser = utils.CmdParser()
    args = cmdParser.get_args()
    
    hosts = []
    for host in Host.hosts_list(args.host):
        hosts.append(Host(host, args.port))
    
