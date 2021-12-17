import builtwith 
import sys
from colorama import Fore , init
init(convert=True)
def start():
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Web Techs Finder. ')
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
    if 'https' in target.lower():
            pass
    elif 'http' in target.lower():
        pass
    else:
        target = 'http://'+target
    techs = builtwith.parse(target)
    for key in techs:
        i=0
        for value in techs[str(key)]:
            i+=1
            name = key.replace('-', ' ')
            name=name.title()
            if i==2:
                val = val + ' , '+value
                i-=1
                continue
            val = str(value)
        print(Fore.YELLOW+name+' : '+Fore.GREEN+val)
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()


