import sys
import requests

sites = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Instagram": "https://www.instagram.com/{}",
}

def username_search(username):
    print(f"\nSearching for username: {username}\n")

    for site, url in sites.items():
        r = requests.get(url.format(username))

        if r.status_code == 200:
            print(f"[+] Found on {site}: {url.format(username)}")
        else:
            print(f"[-] Not found on {site}")

if len(sys.argv) < 3:
    print("Usage: python main.py username <target>")
    sys.exit()

command = sys.argv[1]
target = sys.argv[2]

if command == "username":
    username_search(target)
