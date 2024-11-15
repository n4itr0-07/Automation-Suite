import requests        # Importing the requests library to make HTTP requests
import sys             # Importing sys to retrieve command-line arguments
from time import sleep # Importing sleep for smooth effects
from colorama import Fore, Style, init  # Importing colorama for terminal text styling

# Initialize colorama to work across platforms (Windows/Unix)
init(autoreset=True)

# Title Banner with your name "NAITRO 07"
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("============================================")
print("        Subdomain Finder by NAITRO 07       ")
print("============================================")
print(Style.RESET_ALL)

# Load the subdomains list from the file
sub_list = open("subdomains.txt").read()  # Read the file containing subdomains
subdoms = sub_list.splitlines()           # Split each line into an individual subdomain

# Main loop to iterate over each subdomain in the list
for sub in subdoms:
    # Create the URL to test, combining subdomain and main domain from CLI argument
    sub_domains = f"http://{sub}.{sys.argv[1]}"
    
    try:
        # Attempt to connect to the subdomain
        response = requests.get(sub_domains)

    except requests.ConnectionError:
        # If connection fails, continue without printing anything
        print(f"{Fore.RED}[-] Invalid domain: {sub_domains}")
        sleep(0.1)  # Small delay for smooth output

    else:
        # If connection is successful, print the valid domain in green
        print(f"{Fore.GREEN}[+] Valid domain found: {sub_domains}")
        sleep(0.1)  # Small delay for smooth output

# End message
print(f"{Fore.MAGENTA}\nScan Complete! - Crafted by NAITRO 07 {Style.RESET_ALL}")
