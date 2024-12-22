
import socket
import termcolor
import argparse

def main():

    parser = argparse.ArgumentParser(description="PortScanner is used to scan for opened ports on given IP addresses")

    parser.add_argument(
        "--ipaddress", "-ip",
        type=str,
        required=True,
        help="IP addresses list to scan, delimited by ',' without whitespace between ex 255.255.255.255,200.200.200.200"
    )

    parser.add_argument(
        "--port", "-p",
        type=int,
        required=True,
        help="Port count to scan. ex -p 80 will scan ports in range of 1-80."
    )

    args = parser.parse_args()

    targets = args.ipaddress
    ports = args.port

    if targets is not None:
        if ',' in args.ipaddress:
            print(termcolor.colored(f"\n[*] Scanning Multiple Targets\n",'green'))
            for ip_addr in targets.split(","):
                scan(ip_addr.strip(' '), ports)
        else:
            scan(targets, ports)
    
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

if __name__ == "__main__":
    main()