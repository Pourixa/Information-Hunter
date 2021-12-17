import requests as r 
from colorama import Fore
import sys
wordlist=open(r'Hacking And Python\extras\adminwl.txt','r')
wordlist=wordlist.read()
wordlist=wordlist.split()

def start():
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Admin Panel Finder. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Web Address. ')
    target=input(Fore.RED+' [~] : ')
    if target == '':
        while True:
            print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Target Web Address. ')
            target=input(Fore.RED+' [~] : ')
            if target!='':
                break
            else:
                continue
    if 'https' in target.lower():
        pass
    elif 'http' in target.lower():
        pass
    else:
        target = 'http://'+target
    if target.endswith('/')==True:
        pass
    else:
        target=target+'/'
        
    for i in wordlist:
        req=r.get(target+str(i))
        if req.status_code==200:
            print(Fore.GREEN+'[+] : Link : ({})'.format(target+i)+Fore.YELLOW+(' | ')+Fore.GREEN+('Found')+Fore.GREEN+'.')
        elif req.status_code!=200 and req.status_code!=404:
            print(Fore.RED+'[-] : Link : ({})'.format(target+i)+Fore.BLUE+(' | ')+Fore.RED+(str(req.status_code))+Fore.RED+'.')
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
