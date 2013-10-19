#!/usr/bin/sh

#
# Mandatory features : 
#

#IPv4 support

python port_scanner.py -H 127.0.0.1

#IPv6 support

python port_scanner.py

#passive scan

python port_scanner.py

#single host scan, with single + multiport scan

python port_scanner.py -H 127.0.0.1 -P 80
python port_scanner.py -H 127.0.0.1 -P 80,21
python port_scanner.py -H 127.0.0.1 -P 0-1023

#range scanning (IP + ports)

python port_scanner.py

#listing ports state (closed/open/filtered)

python port_scanner.py

#semi-quiet mode for ports state (open/filtered only)

python port_scanner.py
