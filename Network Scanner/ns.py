#!/usr/bin/env python
from scapy.all import ARP, Ether, srp, ls

def scan(ip):
    ar = ARP(pdst=ip) # ar means arp request, creating a arp request 
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") # seting destination mac to broadcast mac
    arb = broadcast/ar # Combining broadcast and arp request together
    ans = srp(arb, timeout=5, verbose=False)[0] # srp is used to send packets, ans = location where answered packets are stored, unans = location where unanswered packets are stored.
    print("\nIP\t\tMac Address\n-------------------------------------")

    for element in ans:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        
get_ip = input("Enter An IP Like 192.168.1.1 or 192.168.1.1/24: ")
scan(get_ip)