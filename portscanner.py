
---

### 🐍 `portscanner.py` (basic version for now and I m tryn to add somme useful features ....)
import socket
import threading
import argparse
from datetime import datetime

def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is open")
        with open("results/scan_report.txt", "a") as f:
            f.write(f"Port {port} is open\n")
        sock.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("--host", required=True, help="Target IP or domain")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    args = parser.parse_args()

    target_ip = socket.gethostbyname(args.host)
    print(f"Scanning {args.host} ({target_ip}) from port {args.start} to {args.end}")
    print(f"Started at {datetime.now()}\n")

    for port in range(args.start, args.end + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()

if __name__ == "__main__":
    main()
