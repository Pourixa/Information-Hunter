import sys
import os
import time
import menu
from modules import adminfinder,directorybf,dnslookup,httpheader,iplocation,reverseip,subdomainfinder,traceroute,webtechs,wordpressplugin,wordpressusername
from colorama import Fore
while True:
    try:
        menu.clear()
        menu.banner()
        menu.menu0()
        choice=int(input(Fore.RED+' [~] : '))
        if choice==3:
            print(Fore.YELLOW+'\n [*] Good Luck')
            sys.exit()
        #cms
        elif choice==2:
            while True:
                menu.clear()
                menu.banner()
                menu.menucms()
                choice=int(input(Fore.RED+' [~] : '))
                if choice==1:
                    menu.clear()
                    menu.banner()
                    wordpressplugin.start()
                elif choice==2:
                    menu.clear()
                    menu.banner()
                    wordpressusername.start()
                elif choice==3:
                    break
                else:
                    print(Fore.RED+' [!] Wrong input. ')
                    time.sleep(2)
                    continue
        #Information Ghatering
        elif choice==1:
            while True:
                menu.clear()
                menu.banner()
                menu.menuig()
                choice=int(input(Fore.RED+' [~] : '))                                          
                if choice == 1:
                    menu.clear()
                    menu.banner()
                    adminfinder.start()
                elif choice==2:
                    menu.clear()
                    menu.banner()
                    directorybf.start()
                elif choice==3:
                    menu.clear()
                    menu.banner()
                    dnslookup.start()
                elif choice==4:
                    menu.clear()
                    menu.banner()
                    httpheader.start()
                elif choice==5:
                    menu.clear()
                    menu.banner()
                    iplocation.start()
                elif choice==6:
                    menu.clear()
                    menu.banner()
                    reverseip.start()
                elif choice==7:
                    menu.clear()
                    menu.banner()
                    subdomainfinder.start()
                elif choice==8:
                    menu.clear()
                    menu.banner()
                    traceroute.start()
                elif choice==9:
                    menu.clear()
                    menu.banner()
                    webtechs.start()
                elif choice==0:
                    break
                else:
                    print(Fore.RED+' [!] Wrong input. ')
                    time.sleep(2)
                    continue
        else:
            print(Fore.RED+' [!] Wrong input. ')
            time.sleep(3)
    except Exception as e:
        print(e)
        print(Fore.YELLOW+'\n [*] Good Luck')
        sys.exit()