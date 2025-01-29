import requests
import socket
import time
import json
import struct
import os

#1:check the Host is online or offline:
def calculate_checksum(packet):
    if len(packet) % 2 == 1:
        packet += b'\0'
    checksum = sum(struct.unpack("!%dH" % (len(packet) // 2), packet))
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum += checksum >> 16
    return ~checksum & 0xFFFF

#ICMP Echo Request
def create_icmp_packet(id, seq):

    header = struct.pack("!BBHHH", 8, 0, 0, id, seq)
    data = struct.pack("d", time.time())  
    checksum = calculate_checksum(header + data)
    header = struct.pack("!BBHHH", 8, 0, checksum, id, seq)
    return header + data


def check_host_online_icmp(host):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        print("Please run this script with administrative privileges.")
        return False

    sock.settimeout(1)
    packet_id = os.getpid() & 0xFFFF 
    packet_seq = 1  
    packet = create_icmp_packet(packet_id, packet_seq)

    try:
        sock.sendto(packet, (host, 1))
        start_time = time.time()
        response, _ = sock.recvfrom(1024)
        end_time = time.time()
    except socket.timeout:
        print(f"{host} is offline.")
        return False

    icmp_header = response[20:28]
    icmp_type, _, _, recv_id, _ = struct.unpack("!BBHHH", icmp_header)
    if icmp_type == 0 and recv_id == packet_id:  
        print(f"{host} is online. Response time: {(end_time - start_time) * 1000:.2f} ms")
        return True
    else:
        print(f"{host} is offline.")
        return False


        
host = input("enter your Host that you want to check ?")
check_host_online_icmp(host)
