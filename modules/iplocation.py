from colorama import Fore
import ipapi
import socket
import sys
TLD=open('extras/toplevelnames.txt','r')
TLD=TLD.read()
TLD=TLD.split()
infoip=None
def start():
    print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To IP Information. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target IP Address. ')
    print(Fore.CYAN+' [!] '+Fore.GREEN+' Or Leave Input Empty And Press Enter To Get Ur IP Information. ')
    target=input(Fore.RED+' [~] : ')
    info = ipapi.location(ip=target, key=None)
    while True:
        info = ipapi.location(ip=target, key=None)
        try:
                
        # try:
        #     for i in TLD:
        #         res=target.endswith(str(i))
        #         if res==True:
        #             IP=socket.gethostbyname(target)
        #             infoip=ipapi.location(ip=IP ,key=None)
        #             break
        #     info = ipapi.location(ip=target, key=None)
        #     if infoip!=None:
        #         print(Fore.GREEN+' [!] Information. ')
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' IP : '+ infoip['ip'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Version : '+infoip['version'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Region : '+ infoip['region'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Region Code : '+ infoip['region_code'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Name : '+ infoip['country_name'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Capital : '+ infoip['country_capital'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Country TLD : '+ infoip['country_tld'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Calling Code : '+ infoip['country_calling_code'])
        #         print(Fore.GREEN+'[!]'+Fore.CYAN+' ORG : '+ infoip['org'])
                print(Fore.GREEN+' [!] Information. ')
                print(Fore.GREEN+'[!]'+Fore.CYAN+' IP : '+ info['ip'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Version : '+info['version'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Region : '+ info['region'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Region Code : '+ info['region_code'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Name : '+ info['country_name'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Capital : '+ info['country_capital'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Country TLD : '+ info['country_tld'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' Country Calling Code : '+ info['country_calling_code'])
                print(Fore.GREEN+'[!]'+Fore.CYAN+' ORG : '+ info['org'])
                break
        except Exception as e:
            if e==KeyError:
                print(Fore.RED+' [!] Please Enter IP Address')
                print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Target IP Address. ')
                print(Fore.CYAN+' [!] '+Fore.GREEN+' Or Leave Input Empty And Press Enter To Get Ur IP Information. ')
                target=input(Fore.RED+' [~] : ')
                continue
            else:
                break
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
