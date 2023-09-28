#!/usr/bin/env python
from scapy.all import ARP, Ether, srp, ls
from argparse import ArgumentParser
def scan(ip):
    ar = ARP(pdst=ip) # ar means arp request, creating a arp request 
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") # seting destination mac to broadcast mac
    arb = broadcast/ar # Combining broadcast and arp request together
    ans = srp(arb, timeout=5, verbose=False)[0] # srp is used to send packets, ans = location where answered packets are stored, unans = location where unanswered packets are stored.
    
    #ls(ans)

    el = [] # Empty List Used By dict (Dictionary Inside Loop) Appending Information.

# Below Loop will intrate over the list of responses that are recived, ans contains the the list of responded hosts 
    for element in ans:
# dictionary to store IP in ip key and Mac in mac key
        dict = {"ip": element[1].psrc, "mac" : element[1].hwsrc}
        el.append(dict) # Appending dict(dictionary) to el(empty list).

# [1] will help us in fethching only the information we need from the list, [1] is index.
        #print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return el

def pr(resl): #function to print the result, pr means print result and resl means results list.
    print("\nIP\t\t\tMac Address\n-------------------------------------")
    for clients in resl:
        print(clients["ip"] + "\t\t" + clients["mac"])

def get_args(): # used to get arguments directly from terminal
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP Range")
    return parser.parse_args()
    
 
#get_ip = input("Enter An IP Like 192.168.1.1 or 192.168.1.1/24: ")
# Comment Whole get_args() function and 38th Line Before Uncommenting Below Code.
# pr(scan(input("Enter An IP Like 192.168.1.1 or 192.168.1.1/24: "))) #
pr(scan(get_args().target)) #
#print(scan_results)