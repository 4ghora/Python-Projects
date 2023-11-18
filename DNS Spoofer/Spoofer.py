#!/usr/bin/env python

import netfilterqueue

def process_packet(packet):
    print(packet)

    # accept will forward the requests
    # drop will drop the requests, this is disconnect the victim from accessing the internet.
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()



## Terminals Commands
# iptables -I FORWARD -j NFQUEUE --queue-num 0
    ## Use FORWARD chian while attacking a remote computer
    ## Use INPUT AND OUTPUT chains for local testing

# iptables --flush
    ## Execute After stopping the Program
