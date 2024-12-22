
import socket
import termcolor

def scan(target, ports):
    print(f"Starting Scan For {target}:\n")
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"\t[+] Port Opened {ipaddress}:{port}")
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets To Scan (Split them by ','): ")
ports = int(input("[*] Enter How Many Ports Do You Want To Scan: "))

if ',' in targets:
    print(termcolor.colored(f"\n[*] Scanning Multiple Targets\n",'green'))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
