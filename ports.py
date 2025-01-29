import socket
import time
import os
#Checking the status of open or closed host ports
def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} on {host} is open.")
            else:
                print(f"Port {port} on {host} is closed.")
    return open_ports

#Calculate the response delay time for a specific port:
def measure_latency(host, port, num_requests=5):
    latencies = []
    for i in range(num_requests):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            start_time = time.time()
            #time.perf_counter()
            result = sock.connect_ex((host, port))
            end_time = time.time()
            if result == 0:
                latency = end_time - start_time
                latencies.append(latency)
                print(f"Request {i+1}: Latency for port {port} on {host} is {latency:.4f} seconds.")
            else:
                print(f"Request {i+1}: Port {port} on {host} is closed.")
    average_latency = sum(latencies) / len(latencies) if latencies else None
    if average_latency:
        print(f"Average latency for port {port} on {host} is {average_latency:.4f} seconds.")
    return average_latency
host=input("enter your hostname :")
start_port = int(input("Enter the starting port number for scanning: "))
end_port = int(input("Enter the ending port number for scanning: "))
scan_ports(host, start_port, end_port)
measure_latency(host, 80)

