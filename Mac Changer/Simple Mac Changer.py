#!/usr/bin/env python
import subprocess   # Subprocess modules accepts, runs and returns the output of the system commands.
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, Use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, Use --help for more info")
    return parser.parse_args()

def mac_changer(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " and New Mac is " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])   
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])   
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
mac_changer(options.interface, options.new_mac)


''' OLD CODE

print("[+] Changing MAC Address for " + interface + " and New Mac is " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

'''

