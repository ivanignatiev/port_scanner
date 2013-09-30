import sys
import argparse

class CmdParser(argparse.ArgumentParser):
    def __init__(self):
        super(CmdParser, self).__init__("Light nmap implementation\n")
        
    def error(self):
        self.print_help()
        sys.exit(2)
        
    def get_args(self):
        args = sys.argv
        try:
            self.add_argument("-H", "--host", type=int,
                              help="""Host name, IP address.
                              Could be either ipv4 or ipv6.
                              -ipv4 have to be in the folowing form:
                                X.X.X.X where X is a decimal number.
                              -ipv6 have to be in the folowing form:
                                xXxX:xXxX:xXxX:xXxX:xXxX:xXxX:xXxX:xXxX
                              where x and X are hexadecimal numbers.
                              """, metavar="", required=True)
            self.add_argument("-p", "--passive", help="Passive scan mode", metavar="")
            self.add_argument("-s", "--quiet", help="Semi-quiet mode", metavar="")
            args = vars(self.parse_args())
        except TypeError:
            print ("Given argument(s) is/are incorrect. Usage is as follow:")
            self.print_help()
        return args
        
    def parse_ip(self, ipAddress):
        occurences = ipAddress.count('.')
        if occurences == 0:
            occurences = ipAddress.count(':')
            if occurences == 0:
                return ""
            return "ipv6"
        return "ipv4"
            