import socket
import termcolor


def scan(target, ports):
    print(termcolor.colored(f'\n[*] Scanning target: {target}', 'green'))
    for port in range(1, ports):
        port_scanner(target, port)


def port_scanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'[+] Port Opened {port}')
        sock.close()
    except:
        pass


targets = input('[*] Enter Targets to Scan(split targets by ,): ')
ports = int(input('[*] Enter How Many Ports You Want to Scan: '))

if ',' in targets:
    print(termcolor.colored('[*] Scanning Multiple Targets', 'green'))
    for target in targets.split(','):
        scan(target.strip(' '), ports)
else:
    scan(targets, ports)
