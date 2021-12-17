import requests
import sys
from colorama import Fore 

def start():
    try:
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Http Header Check. ')
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Note: We Use HackerTarget API For This Tool. ')
        print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Website Address. ')
        target=input(Fore.RED+' [~] : ')
        if target == '':
            while True:
                print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Target Website Address. ')
                target=input(Fore.RED+' [~] : ')
                if target!='':
                    break
                else:
                    continue
        result=requests.get('https://api.hackertarget.com/httpheaders/?q='+target).text
        print(Fore.GREEN+result)
    except ConnectionError:
        print(Fore.RED+' [!] '+'Please Check Your Connection..')
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
