import requests
import concurrent.futures
from colorama import Style, Fore,init
init(autoreset=True)

# ================================================
#          AYOBBARNVA SUBDOMAIN FINDER
# ================================================

print(Fore.CYAN + Style.BRIGHT + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     █████╗ ██╗   ██╗  ██████╗ ██████╗                      ║
║    ██╔══██╗╚██╗ ██╔╝ ██╔═══██╗██╔══██╗                     ║
║    ███████║ ╚████╔╝  ██║   ██║██████╔╝                     ║
║    ██╔══██║  ╚██╔╝   ██║   ██║██╔══██╗                     ║
║    ██║  ██║   ██║    ╚██████╔╝██████╔╝                     ║
║    ╚═╝  ╚═╝   ╚═╝     ╚═════╝ ╚═════╝                      ║
║                                                            ║
║                      By: Ayobbarnva                        ║
║             https://github.com/ayobbarnva                  ║
║                 Subdomain Brute Forcer                     ║
╚════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)
url = input(Fore.GREEN+'url >>>')
subs_1 = open('domains.txt', 'r')
subs = subs_1.readlines()
print(Fore.MAGENTA+'There is no end')
with open(f'{url}_result.txt','w') as e:
    e.writelines('')
def check_sub(lines):
    sub = lines.strip()
    try:
        request = requests.get('https://' + sub + '.' + url,timeout=5)
        if request.status_code==200:
            result=sub + '.' + url+' '
            print(Fore.CYAN+result)
            
            with open(f'{url}_result.txt','+a') as a:
                a.writelines(result+'\n')
    except:
        pass
try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(check_sub, subs)
except KeyboardInterrupt:
    print(Fore.RED+'finish file save to result.txt')
