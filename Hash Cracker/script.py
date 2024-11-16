import hashlib       # Import hashlib for MD5 hashing
from colorama import Fore, Style, init  # Import colorama for colorful terminal output
from time import sleep # Import sleep to control output speed

# Initialize colorama for cross-platform color support
init(autoreset=True)

# Display tool name and author
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("==============================================")
print("       MD5 Hash Cracker by NAITRO 07")
print("==============================================")
print(Style.RESET_ALL)

# Prompt user for wordlist file location and hash input
wordlist_location = input(f"{Fore.YELLOW}Enter wordlist file location: {Style.RESET_ALL}")
hash_input = input(f"{Fore.YELLOW}Enter MD5 hash to be cracked: {Style.RESET_ALL}")

# Try opening and reading the wordlist file
try:
    with open(wordlist_location, 'r') as file:
        # Flag to check if password is found
        found = False

        # Iterate over each line in the wordlist
        for line in file.readlines():
            # Generate MD5 hash for each line (password attempt)
            hash_ob = hashlib.md5(line.strip().encode())
            hashed_pass = hash_ob.hexdigest()
            
            # Display progress in a non-intrusive way
            print(f"{Fore.YELLOW}Trying password: {line.strip()}{Style.RESET_ALL}", end='\r')
            sleep(0.1)  # Slow down for visibility
            
            # Check if the generated hash matches the input hash
            if hashed_pass == hash_input:
                print(f"\n{Fore.GREEN}[+] Found cleartext password: {line.strip()}{Style.RESET_ALL}")
                found = True
                break

        # If no match is found, inform the user
        if not found:
            print(f"\n{Fore.RED}[-] Password not found in wordlist.{Style.RESET_ALL}")

except FileNotFoundError:
    # Handle case where wordlist file is not found
    print(f"{Fore.RED}Error: Wordlist file '{wordlist_location}' not found. Please check the file path and try again.{Style.RESET_ALL}")
except Exception as e:
    # Handle any other exceptions that may occur
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
