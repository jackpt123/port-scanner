import socket
from IPy import IP

def scan(target, port_num):
    converted_ip = check_ip(target)
    print("\n" + "[scanning target...] " + str(target))
    port_num2 = port_num + 1
    for port in range(1, port_num2):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.2)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port " + str(port) + " : " + str(banner.decode().strip("\n")))
        except:
            print("[+] Open Port " + str(port))
    except:
        pass

targets = input("[A] Enter target/s to scan: (split multiple targets with a comma) : ")
port_num = int(input("Enter number of ports you want to scan: "))
if "," in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(" "), port_num)
else:
    scan(targets, port_num)