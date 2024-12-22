
import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened {ipaddress}:{port}")
        sock.close()
    except:
        print(f"[-] Port closed {ipaddress}:{port}")

targets = input("[*] Enter Targets To Scan (Split them by ','): ")
ports = int(input("[*] Enter How Many Ports Do You Want To Scan: "))

if ',' in targets:
    print(f"[*] Scanning Multiple Targets")
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
