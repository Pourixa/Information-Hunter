import subprocess
import platform
import sys
from colorama import Fore 
def start():
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Trace Route. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target IP/Domain. ')
    target=input(Fore.RED+' [~] : ')
    print(Fore.GREEN+'')
    os=platform.uname()
    if os[0].lower()=='windows':
        subprocess.call('tracert '+target)
    elif os[0].lower()=='linux':
        subprocess.call('traceroute '+target)
    else:
        subprocess.call('traceroute '+target)
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
