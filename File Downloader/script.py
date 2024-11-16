import requests        # Import requests for HTTP handling
from time import sleep # Import sleep to add delays for smooth output
from colorama import Fore, Style, init  # Import colorama for terminal styling

# Initialize colorama for color support across platforms
init(autoreset=True)

# Display a banner with your name
print(f"{Fore.CYAN}{Style.BRIGHT}")
print("==============================================")
print("          File Downloader by NAITRO 07        ")
print("==============================================")
print(Style.RESET_ALL)

# List to store files to download (with URLs and file names)
files_to_download = []

# User Input Loop
while True:
    # Ask the user for the URL
    file_url = input(f"{Fore.YELLOW}Enter the URL of the file to download: {Style.RESET_ALL}")
    
    # Ask the user for the filename to save as
    filename = input(f"{Fore.YELLOW}Enter the filename to save as (with extension): {Style.RESET_ALL}")
    
    # Add the file details to the download list
    files_to_download.append({'url': file_url, 'filename': filename})
    
    # Ask if the user wants to add another file
    another = input(f"{Fore.CYAN}Would you like to add another file? (yes/no): {Style.RESET_ALL}")
    if another.lower() != 'yes':
        break

# Function to download a file and save it locally
def download_file(file_url, filename):
    print(f"{Fore.YELLOW}[~] Starting download: {filename} from {file_url}")
    
    try:
        # Make a GET request to download the file
        response = requests.get(file_url, allow_redirects=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)  # Save the file content
            print(f"{Fore.GREEN}[+] Download complete: {filename}\n")
        else:
            print(f"{Fore.RED}[-] Failed to download {filename}: HTTP {response.status_code}")
    
    except requests.RequestException as e:
        # Handle any request errors
        print(f"{Fore.RED}Error downloading {filename}: {e}")

# Loop through each file in the user-provided list and download it
for file in files_to_download:
    download_file(file['url'], file['filename'])
    sleep(0.5)  # Small delay for smoother output between downloads

# Final message after all downloads
print(f"{Fore.MAGENTA}All downloads complete! - Powered by NAITRO 07 {Style.RESET_ALL}")
