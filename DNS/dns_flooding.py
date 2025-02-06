import subprocess
import argparse

def run_dnsperf(target_ip):
    try:
        command = ["dnsperf", "-s", target_ip, "-p", "1053", "-d", "domains.txt", "-l", "900", "-Q", "10000"]
        print(f"Executing command: {' '.join(command)}")  # Debug output
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running dnsperf: {e}")
    except FileNotFoundError:
        print("Error: dnsperf is not installed. Please install it and try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run dnsperf with a specified target IP.")
    parser.add_argument("target_ip", help="The IP address of the target DNS server")
    args = parser.parse_args()
    
    run_dnsperf(args.target_ip)
