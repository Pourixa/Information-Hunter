import requests
import sys
import time
from colorama import Fore

list= ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def start():
    try:
        print(Fore.CYAN+' [!] '+Fore.YELLOW+' Welcome To Directory Brute Force. ')
        print(Fore.CYAN+' [!] '+Fore.GREEN+' Please Enter Website Address. ')
        target=input(Fore.RED+' [~] : ')
        if target == '':
            while True:
                print(Fore.CYAN+' [!] '+Fore.RED+' Please Enter Website Address. ')
                target=input(Fore.RED+' [~] : ')
                if target!='':
                    break
                else:
                    continue
        if 'http' in target.lower():
            pass
        else:
            target='http://'+target
            
        for i in list:
            time.sleep(0.1)
            url=target+'/'+i
            req= requests.get(url)
            if req.status_code==200 or req.status_code==405:
                print(Fore.GREEN+' [+] ' + url)
            else:
                print(Fore.RED+' [-] ' + url)
    except:
        pass
    try:
        input(Fore.RED+' [*]: Back To Menu (Press Enter). ')
    except:
        sys.exit()
