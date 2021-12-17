import socket 
import sys
from colorama import Fore , init
init(convert=True)
def start():
    subs=open('extras/toplevelnames.txt','r')
    subs=subs.read()
    subs=str(subs).split()
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Subdomain Finder. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Website Address. ')
    address=input(Fore.RED+' [~] : ')
    while True:
        if address =='':
                print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target Website Address. ')
                address=input(Fore.RED+'[~]: ')
        else:
            break
    ip = socket.gethostbyname(address)
    ip0=ip
    for sub in subs:
        try:
            hosts=(sub)+'.'+address
            ip = socket.gethostbyname(hosts)
            if ip!=ip0:
                print(Fore.RED+'[/] : Host IP : ({})'.format(ip)+Fore.BLUE+(' | ')+Fore.RED+(hosts)+Fore.RED+'.')
            else:
                print(Fore.GREEN+'[+] : Host IP : ({})'.format(ip)+Fore.YELLOW+(' | ')+Fore.GREEN+(hosts)+Fore.GREEN+'.')    
                ip0=ip
        except Exception:
            pass
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()

