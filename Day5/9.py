# Write a python program to check valid IPV4 and IPV6 ip address (Regex) 
import re


def ipv4(ip_address):
    ipv4_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    match = re.match(ipv4_pattern, ip_address)
    return bool(match)

def ipv6(ip_address):
    ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    match = re.match(ipv6_pattern, ip_address)
    return bool(match)

def abc():
    ip_address = input("Enter an IP address: ")
    if ipv4(ip_address):
        print("Valid IPv4 address.")
    elif ipv6(ip_address):
        print("Valid IPv6 address.")
    else:
        print("Invalid IP address.")

abc()
