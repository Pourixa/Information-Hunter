import os 
import requests
import json
from colorama import Fore
import sys

def start():
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Reverse IP Lookup. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target IP/Domain. ')
    target=input(Fore.RED+' [~] : ')
    if target == '':
            while True:
                print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Target IP/Domain. ')
                target=input(Fore.RED+' [~] : ')
                if target!='':
                    break
                else:
                    continue
    data={'remoteAddress':target}
    link= requests.post('https://domains.yougetsignal.com/domains.php',data)
    source = json.loads(link.content)
    for data in source['domainArray']:
        print(''+data[0]+'\n')
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
