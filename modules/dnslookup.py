import requests
import sys
from colorama import Fore 

def start():
    try:
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To DNS Look Up. ')
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Note: We Use HackerTarget API For This Tool. ')
        print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Domain. ')
        target=input(Fore.RED+' [~] : ')
        if target == '':
            while True:
                print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Target Domain. ')
                target=input(Fore.RED+' [~] : ')
                if target!='':
                    break
                else:
                    continue
        result=requests.get('https://api.hackertarget.com/dnslookup/?q='+target).text
        if 'reverse dns tool' in result.lower():
            while True:
                print(Fore.YELLOW+' [!] '+' Please Enter Domain Not IP Address.')
                print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Domain. ')
                target=input(Fore.RED+' [~] : ')
                result=requests.get('https://api.hackertarget.com/dnslookup/?q='+target).text
                if not 'reverse dns tool' in result:
                    break
        print(Fore.GREEN+result)
    except ConnectionError:
        print(Fore.RED+' [!] '+'Please Check Your Connection..')
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
