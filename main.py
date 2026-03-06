import argparse
import requests
import whois
from colorama import Fore, init

init()

banner = """
   ____   _____ _____ _   _ ______ _____  
  / __ \ / ____|_   _| \ | |  ____|  __ \ 
 | |  | | (___   | | |  \| | |__  | |__) |
 | |  | |\___ \  | | | . ` |  __| |  _  /
 | |__| |____) |_| |_| |\  | |____| | \ \ 
  \____/|_____/|_____|_| \_|______|_|  \_\

        STINGER OSINT TOOLKIT
"""

print(Fore.CYAN + banner)


def username_search(username):
    sites = {
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Instagram": "https://www.instagram.com/{}",
    }

    print(Fore.YELLOW + f"\nSearching username: {username}\n")

    for site, url in sites.items():
        r = requests.get(url.format(username))

        if r.status_code == 200:
            print(Fore.GREEN + f"[+] Found on {site}: {url.format(username)}")
        else:
            print(Fore.RED + f"[-] Not found on {site}")


def ip_lookup(ip):
    print(Fore.YELLOW + f"\nInvestigating IP: {ip}\n")

    r = requests.get(f"https://ipinfo.io/{ip}/json")
    data = r.json()

    for key, value in data.items():
        print(Fore.GREEN + f"{key}: {value}")


def domain_lookup(domain):
    print(Fore.YELLOW + f"\nInvestigating domain: {domain}\n")

    info = whois.whois(domain)

    print(Fore.GREEN + f"Registrar: {info.registrar}")
    print(Fore.GREEN + f"Creation Date: {info.creation_date}")
    print(Fore.GREEN + f"Expiration Date: {info.expiration_date}")


parser = argparse.ArgumentParser(description="OSINT Investigation Toolkit")

parser.add_argument("--username", help="Search username across sites")
parser.add_argument("--ip", help="Lookup IP information")
parser.add_argument("--domain", help="Lookup domain WHOIS info")

args = parser.parse_args()

if args.username:
    username_search(args.username)

elif args.ip:
    ip_lookup(args.ip)

elif args.domain:
    domain_lookup(args.domain)

else:
    print("Use --help for options")
