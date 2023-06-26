from scapy.all import *
#from scapy.layers.http import HTTP
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Network traffic filter')
parser.add_argument('pcap_file', help='Path to the input pcap file')
args = parser.parse_args()

# Define filters for each protocol
dns_filter = lambda pkt: pkt.haslayer(DNS)
http_filter = lambda pkt: pkt.haslayer(HTTP)
dhcp_filter = lambda pkt: pkt.haslayer(DHCP)

# Capture packets from pcap file
packets = sniff(offline=args.pcap_file)

while(True):
    Con = input("Which packets you want to filter in this PCAP file:")
    if Con.lower() in ["dns","dhcp","http"]:
        break

if (Con.lower() == "dns"):
    # Print DNS packets
    print("DNS packets:")
    for packet in packets:
        if dns_filter(packet):
            print(packet.summary())
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            print(f"DHCP packet from {src_mac} ({src_ip}:{src_port}) to {dst_mac} ({dst_ip}:{dst_port})")

if (Con.lower() == "http"):
# Print HTTP packets
    print("HTTP packets:")
    for packet in packets:
        if http_filter(packet):
            print(packet.summary())
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            print(f"DHCP packet from {src_mac} ({src_ip}:{src_port}) to {dst_mac} ({dst_ip}:{dst_port})")

if (Con.lower() == "dhcp"):
    # Print DHCP packets
    print("DHCP packets:")
    for packet in packets:
        if dhcp_filter(packet):
            print(packet.summary())
            src_mac = packet[Ether].src
            dst_mac = packet[Ether].dst
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

            print(f"DHCP packet from {src_mac} ({src_ip}:{src_port}) to {dst_mac} ({dst_ip}:{dst_port})")
