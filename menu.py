import os
from colorama import Fore
import time
import sys
import platform
import subprocess
def clear():
    os=platform.uname()
    if os[0].lower()=='windows':
        subprocess.call('cls', shell=True)
    elif os[0].lower()=='linux':
        subprocess.call('clear')
    else:
        subprocess.call('clear')
clear()
def banner():
    print(Fore.LIGHTBLACK_EX+
'''
██╗███╗   ██╗███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗    
██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    
██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║    
██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║    
██║██║ ╚████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║    
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                               
            ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗                             
            ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗                            
            ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝                            
            ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗                            
            ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║                            
            ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
            ||||||||||||||||||||||||||||||||||||||||||||||||||||
            |     This Tool Is Used To Collect Information     |                                                   * 
            |         Programmer : Nemesis(NEM3S1S)            |
            |            Hope You Enjoy Using It               | 
            ||||||||||||||||||||||||||||||||||||||||||||||||||||
''')                           
def menu0():
    time.sleep(0.01)
    print(Fore.YELLOW+' [!] Choice One Of Options Below. \n')
    time.sleep(0.01)
    print(Fore.LIGHTRED_EX+' [1] Information Ghatering. \n')                                                                                          
    time.sleep(0.01)
    print(Fore.LIGHTMAGENTA_EX+' [2] WordPress CMS Detection. \n')  
    time.sleep(0.01)
    print(Fore.YELLOW+' [3] Exit. \n')  
def menucms():
    time.sleep(0.01)
    print(Fore.YELLOW+' [!] Choice One Of Options Below. \n')
    time.sleep(0.01)
    print(Fore.CYAN+' [1] Word Press Plugins Finder. \n')                                                                                          
    time.sleep(0.01)
    print(Fore.LIGHTMAGENTA_EX+' [2] WordPress Username Finder. \n')  
    time.sleep(0.01)
    print(Fore.RED+' [3]: Back To Menu \n') 
def menuig():
    time.sleep(0.01)
    print(Fore.YELLOW+' [!] Choice One Of Options Below. \n')
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [1] Admin Page Finder. \n')                                                                                          
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [2] Website Directory Finder. \n')  
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [3] DNS Look Up. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [4] HTTP Headers. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [5] IP Location Finder. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [6] Reverse IP Check. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [7] Subdomain Finder. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [8] Trace Route. \n') 
    time.sleep(0.01)
    print(Fore.LIGHTCYAN_EX+' [9] Web Technology Detector. \n') 
    time.sleep(0.01)
    print(Fore.RED+' [0]: Back To Menu \n') 