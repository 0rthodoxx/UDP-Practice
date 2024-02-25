import socket
import sys
from datetime import datetime
import ipaddress
import time

# Gets host
HOST = sys.argv[1] if len(sys.argv) == 2 else None
if HOST is None: 
    print(f"*** Invalid call to program ***\nUsage: python3 {sys.argv[0]} <target IP>")
    sys.exit(1)
if HOST.upper() == "LOCALHOST": HOST = "127.0.0.1"
PORT = 12000

try:
    ipaddress.ip_address(HOST)
except:
    print(f"{HOST} is not a valid target")
    sys.exit(1)

socket.setdefaulttimeout(1)
print(f"[+] Starting scan at {datetime.now()}")
for i in range(1, 11):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = f"Ping {i}"
    start_time = time.perf_counter()
    s.sendto(packet.encode(), (HOST, PORT))
    try:
        data, _ = s.recvfrom(1024)
        end_time = time.perf_counter()
        rtt = format((end_time - start_time) * 1000, '.3f')
        print(f"{data.decode()} rtt={rtt} ms")
    except socket.timeout:
        print("Request timed out")
    except Exception as e:
        print(e)    

print(f"[+] Scan completed at {datetime.now()}")
sys.exit(0)

