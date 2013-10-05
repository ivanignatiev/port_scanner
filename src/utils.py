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
            if len(args) <= 1:
                raise TypeError
            args = self.parse_args()
            print ("Yo!")
            print (args.host)
        except TypeError:
            print ("Given argument(s) is/are incorrect. Usage is as follow:")
            self.print_help()
            sys.exit(2)
        return args