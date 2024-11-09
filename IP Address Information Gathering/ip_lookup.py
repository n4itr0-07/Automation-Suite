import os
import urllib.request as urllib2
import json
from colorama import Fore, Style, init #TODO: This is for Colors


# Initialize colorama for color support
init(autoreset=True)

while True:
    ip = input("🌐 Enter the target IP: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    # Display IP info with styling and emojis
    print("\n" + Fore.CYAN + Style.BRIGHT + "🔍 IP Information Lookup 🔍" + Style.RESET_ALL)
    print(Fore.GREEN + "="*30 + Style.RESET_ALL)

    print(Fore.YELLOW + "🌍 IP Address: " + Fore.WHITE + values["query"])
    print(Fore.YELLOW + "🏙️  City: " + Fore.WHITE + values["city"])
    print(Fore.YELLOW + "📡 ISP: " + Fore.WHITE + values["isp"])
    print(Fore.YELLOW + "🌎 Country: " + Fore.WHITE + values["country"])
    print(Fore.YELLOW + "🏞️  Region: " + Fore.WHITE + values["region"])
    print(Fore.YELLOW + "🕒 Timezone: " + Fore.WHITE + values["timezone"])

    print(Fore.GREEN + "="*30 + Style.RESET_ALL)
    print(Fore.CYAN + "✨ End of Information ✨" + Style.RESET_ALL)
    
    break
