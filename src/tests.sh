#!/usr/bin/sh

#
# Mandatory features : 
#

#IPv4 support

python port_scanner.py -H 127.0.0.1

#IPv6 support

python port_scanner.py -H (::1)

#passive scan

python port_scanner.py

#single host scan, with single + multiport scan

python port_scanner.py -H 127.0.0.1 -P 80
python port_scanner.py -H google.com -P 80
python port_scanner.py -H 127.0.0.1 -P 80,21
python port_scanner.py -H 127.0.0.1 -P 0-1023

#range scanning (IP + ports)

python port_scanner.py -H 127.0.0.1:(0-1023)
python port_scanner.py -H (127.0.0.1-127.0.0.2):(0-1023)
python port_scanner.py -H (127.0.0.1-127.0.0.2):(0-10,15),127.0.0.8:80
python port_scanner.py -H (127.0.0.1/30):(0-1023)

#listing ports state (closed/open/filtered)

python port_scanner.py

#semi-quiet mode for ports state (open/filtered only)

python port_scanner.py
