import sys
import argparse
import utils

__author__="godard_b"
__date__ ="$Sep 30, 2013 3:52:38 PM$"

cmdParser = utils.CmdParser()
args = cmdParser.get_args()
print (args[1])
ip = cmdParser.parse_ip(args[1])
print (ip)