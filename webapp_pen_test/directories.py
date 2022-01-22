import requests

target_ip = input('[*] Enter target ip: ')
file_name = input('[*] Enter name of the file containing directories: ')


def request(url):
    try:
        return requests.get(f'http://{url}')
    except requests.exceptions.ConnectionError:
        pass


file = open(file_name, 'r')
for line in file:
    directory = line.strip()
    full_url = f'{target_ip}/{directory}'
    response = request(full_url)
    if response:
        print(f'[*] Discovered directory in path: {full_url}')
