import requests       # Import requests for HTTP requests
import sys            # Import sys for command-line arguments
from time import sleep # Import sleep for delays to smoothen the output
from colorama import Fore, Style, init  # Import colorama for colorful terminal output

# Initialize colorama for automatic reset across different platforms
init(autoreset=True)

# Display a banner with user name and tool purpose
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("============================================")
print("       Directory Enumerator by NAITRO 07     ")
print("============================================")
print(Style.RESET_ALL)

# Check if domain argument is provided
if len(sys.argv) < 2:
    print(f"{Fore.RED}Usage: python script.py <target_domain>")
    sys.exit(1)

# Load directory names from the wordlist file
try:
    sub_list = open("wordlist.txt").read()  # Read the file containing directory names
    directories = sub_list.splitlines()      # Split each line into individual directory names
except FileNotFoundError:
    print(f"{Fore.RED}Error: 'wordlist.txt' file not found. Please create it and add directory names to scan.")
    sys.exit(1)

# Display the target domain and start message
print(f"{Fore.MAGENTA}Target Domain: {sys.argv[1]}")
print(f"{Fore.YELLOW}Starting Directory Enumeration...\n")

# Main loop to iterate over each directory name in the wordlist
for dir in directories:
    # Construct the URL for each directory
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    
    try:
        # Send a GET request to the constructed URL
        r = requests.get(dir_enum)
        
        # Check the response status code to determine if the directory exists
        if r.status_code == 404:
            print(f"{Fore.RED}[-] Not Found: {dir_enum}")
        else:
            print(f"{Fore.GREEN}[+] Valid Directory: {dir_enum}")
    
    except requests.RequestException as e:
        # Handle any network-related errors
        print(f"{Fore.RED}Error connecting to {dir_enum}: {e}")
    
    # Small delay for smoother output, especially with large wordlists
    sleep(0.1)

# Final message
print(f"\n{Fore.CYAN}Scan Complete! - Crafted by NAITRO 07{Style.RESET_ALL}")
