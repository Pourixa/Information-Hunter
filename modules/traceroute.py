import subprocess
import platform
import sys
import os
from colorama import Fore 
def start():
    try:
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Trace Route. ')
        print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target IP/Domain. ')
        target=input(Fore.RED+' [~] : ')
        print(Fore.GREEN+'')
        os1=platform.uname()
        if os1[0].lower()=='windows':
            subprocess.call('tracert '+target)
        elif os1[0].lower()=='linux':
            os.system('traceroute '+target)
        else:
            os.system('traceroute '+target)
    except:
        pass
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
