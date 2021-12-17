
import sys
from time import time
from colorama import Fore
import requests
from time import sleep
import json

def start():
    try:
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To WordPress User Finder. ')
        print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target WordPress URL. ')
        target=input(Fore.RED+' [~] : ')
        if target == '':
                while True:
                    print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Target Domain. ')
                    target=input(Fore.RED+' [~] : ')
                    if target!='':
                        break
                    else:
                        continue
        if 'http' in target.lower():
            req=requests.get(target+'/wp-content/plugins/')
            if req.status_code==404 or req.status_code==500:
                while req.status_code!=404 or req.status_code!=500:
                    print(Fore.RED+' [!] Please Enter A WordPress URL')
                    target=input(Fore.RED+' [~] : ')
                    req=requests.get(target+'/wp-content/plugins/')
                    if 'http' in target.lower():
                        pass
                    else:
                        target='http://'+target
        else:
            target='http://'+target
            req=requests.get(target+'/wp-content/plugins/')
            if req.status_code==404 or req.status_code==500:
                while req.status_code!=404 or req.status_code!=500:
                    print(Fore.RED+' [!] Please Enter A WordPress URL')
                    target=input(Fore.RED+' [~] : ')
                    req=requests.get(target+'/wp-content/plugins/')
                    if 'http' in target.lower():
                        pass
                    else:
                        target='http://'+target
            try:
                r= requests.get(target+'/wp-json/wp/v2/users').text
                j=json.loads(r)
                Count= len(j) -1
                cn=0
                user=''
                for Val in j:
                    Split = '\n'
                    if Count == cn:
                        split=''
                    U=j[cn]['slug']
                    if not U=='':
                        user += Fore.GREEN + ' [+] '+Fore.CYAN+U+Split
                    cn+=1
                if user=='':
                    user=Fore.RED+' [-]  Not Found! '
                print(user)
                
            except:
                pass
    except:
        pass
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
