from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import Ether

def packet_callback(packet):
    if packet.haslayer(Ether):
        ethernet = packet[Ether]
        print("###  Ethernet Frame  ###\n")
        print(f"Source Mac address : {ethernet.src}")
        print(f"Destination Mac address : {ethernet.dst}")
        print(f"Type : {ethernet.type}")
    if packet.haslayer(IP):
        ip = packet[IP] 
        print("###  IP Packet  ###\n")
        print(f"Version: {ip.version}")
        print(f"IP Header Length : {ip.ihl}")
        print(f"Type of service : {ip.tos}")
        print(f"Total length of the packet : {ip.len}")
        print(f"TTL : {ip.ttl}")
        print(f"Flags : {ip.flags}")
        print(f"Fragment offset : {ip.frag}")
        print(f"Protocol : {ip.proto}")
        print(f"Source IP Address : {ip.src}")
        print(f"Destination IP Address : {ip.type}")

        if packet.haslayer(UDP):
            udp = packet[UDP]
            print(f"###  UDP Packet  ###\n")
            print(f"Length: {udp.len}")
            print(f"Checksum: {udp.chksum}")
            print(f"Source Port: {udp.sport}")
            print(f"Destination Port: {udp.dport}")

        elif  packet.haslayer(TCP):
            tcp = packet[TCP]   
            print(f"###  TCP Packet  ###\n")
            print(f"Source Port: {tcp.sport}")
            print(f"Destination Port: {tcp.dport}")
            print(f"Sequence Number: {tcp.seq}")
            print(f"Acknowledgment Number: {tcp.ack}")
            print(f"Flags: {tcp.flags}")
            print(f"Window Size: {tcp.window}")
            print(f"Checksum: {tcp.chksum}")

        elif packet.haslayer(ICMP):
            icmp = packet[ICMP]
            print(f"###  ICMP Packet  ###\n")
            print(f"Type: {icmp.type}")
            print(f"Code: {icmp.code}")
            print(f"Checksum: {icmp.chksum}")
            print(f"Identifier: {icmp.id}")
            print(f"Sequence Number: {icmp.seq}")    
        
def main():
    sniff(prn=packet_callback, store=False)      

if __name__ == "__main__":
    main()
