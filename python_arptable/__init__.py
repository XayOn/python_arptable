# -*- coding: utf-8 -*-
import csv

__author__ = 'David Francos'
__email__ = 'me@davidfrancos.net'
__version__ = '0.0.1'


def get_arp_table():
    """
        Get ARP table from /proc/net/arp
    """
    with open('/proc/net/arp') as arpt:
        names = [
            'IP address', 'HW type', 'Flags', 'HW address', 'Mask', 'Device'
        ]  # arp 1.88, net-tools 1.60

        reader = csv.DictReader(
            arpt, fieldnames=names, skipinitialspace=True, delimiter=' ')

        next(reader)  # Skip header.

        return [block for block in reader]


ARPTABLE = get_arp_table()
