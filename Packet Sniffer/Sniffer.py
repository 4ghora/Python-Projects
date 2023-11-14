#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
      if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode('utf-8', errors='ignore')
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword.lower() in load.lower():
                    return load
                
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(url)
        login_info = get_login_info(packet)
        if login_info:
            print("\nPossible Login Information --> " + login_info + "\n")
            print(url)

try:
    iface = input("Enter Interface: ")
    print(f"Sniffing on {iface}...")
    sniff(iface)
except KeyboardInterrupt:
    print("\nExiting....")

'''

Here is a detailed explanation of the packet sniffer code:

-> Imports

    - scapy.all: Import Scapy packet manipulation library
    - http: Imports Scapy HTTP layer

-> Keywords
-> List of keywords to match in packet load

-> sniff()

    - Starts packet sniffing using Scapy
    - iface: Interface to sniff on
    - store=False: Don't store packets
    - prn: Callback function for processing packets

-> process_sniffed_packet()

    - Callback function that gets called by Scapy for each packet
    - Check for HTTP Request layer using haslayer()
    - Check for Raw load
    - Decode load bytes to UTF-8 string
        - Ignore errors to handle invalid UTF-8
    - Loop through keywords and check if in load
    - Prints load if keyword found

-> Main

    - Get iface input from user
    - Print interface sniffing on
    - Call sniff() to start sniffing
    - Use try/except to handle Ctrl+C KeyboardInterrupt
    - Print exited message on KeyboardInterrupt

So in summary, it takes an interface as input, initializes Scapy sniffing on
that interface with a packet processing callback function and prints any packet 
loads that contain the target keywords.

The callback function decodes the Raw packet load, checks for keywords and prints
matches. This allows customized packet inspection for keywords or patterns.

'''