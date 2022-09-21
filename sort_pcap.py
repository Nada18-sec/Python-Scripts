# Requirements before running the program:
# Install scapy using 'pip install --pre scapy[complete]'

from django.db import connection
from scapy.all import *

packets = rdpcap('Insert name of pcap') #Include the name of your pcap file

connections = set()

for packet in packets:
    if 'IP' in packet:
        ip_layer = packet['IP']
        connections.add((ip_layer.src, ip_layer.dst, ip_layer.dport))
        
# This function will print out the src IP, dest IP and dest Port
for c in connections:
    print(c)