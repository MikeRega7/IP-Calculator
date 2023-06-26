#!/usr/bin/python3

import ipaddress
import sys
import signal
import argparse
from colorama import init, Fore

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

init()

parser = argparse.ArgumentParser()
parser.add_argument("--ip", "-i", type=str, help="IP with CIDR", required=True)
args = parser.parse_args()
ip_network = args.ip

def ip_cal(ip_network):
    network = ipaddress.IPv4Network(ip_network, strict=False)
    print("IP: ", Fore.GREEN + str(network.network_address) + Fore.RESET)
    print("Netmask: ", Fore.YELLOW + str(network.netmask) + Fore.RESET)
    print("First IP: ", Fore.BLUE + str(network.network_address) + Fore.RESET)
    print("Last IP: ", Fore.BLUE + str(network.network_address + network.num_addresses - 1) + Fore.RESET)
    print("Broadcast (Last IP): ", Fore.BLUE + str(network.broadcast_address) + Fore.RESET)
    print("Total de hosts: ", Fore.CYAN + str(network.num_addresses) + Fore.RESET)

if __name__ == '__main__':
    ip_cal(ip_network)
