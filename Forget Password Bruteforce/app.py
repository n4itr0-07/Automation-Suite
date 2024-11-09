import requests
import argparse
import random
import logging
import time
from termcolor import colored
import sys

# Beautiful banner
def print_banner():
    banner = """
    █████╗ ██████╗ ███████╗     ███████╗██╗   ██╗███████╗███████╗██████╗ ███╗   ███╗███████╗
   ██╔══██╗██╔══██╗██╔════╝     ██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗████╗ ████║██╔════╝
   ███████║██║  ██║█████╗       ███████╗██║   ██║█████╗  █████╗  ██████╔╝██╔████╔██║█████╗  
   ██╔══██║██║  ██║██╔══╝       ╚════██║██║   ██║██╔══╝  ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══╝  
   ██║  ██║██████╔╝███████╗     ███████║╚██████╔╝███████╗███████╗██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝  ╚═╝╚═════╝ ╚══════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                        
                               API Fuzzer Supreme (AFS)
    """
    print(colored(banner, 'green'))

# Fuzzing logic
def fuzz_api(url, method, headers, params, data, output_file):
    payloads = ["<script>alert(1)</script>", "{'key': 'value'}", "SELECT * FROM users;", "admin'; --", "<img src=x onerror=alert(1)>", 
                "' OR '1'='1", "DROP TABLE users;", "admin", "null", "", "{}"]
    
    for i in range(10):  # Perform 10 fuzz tests
        fuzz_payload = random.choice(payloads)

        # Set the fuzz payload in params, headers, or data
        fuzz_params = {k: fuzz_payload for k in params} if params else None
        fuzz_headers = {k: fuzz_payload for k in headers} if headers else None
        fuzz_data = data.replace("FUZZ", fuzz_payload) if data else None
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=fuzz_headers, params=fuzz_params)
            elif method == 'POST':
                response = requests.post(url, headers=fuzz_headers, params=fuzz_params, data=fuzz_data)
            elif method == 'PUT':
                response = requests.put(url, headers=fuzz_headers, params=fuzz_params, data=fuzz_data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=fuzz_headers, params=fuzz_params)

            # Log the request and response
            log_output = f"Fuzz {i+1}:\n" \
                         f"Method: {method}\n" \
                         f"URL: {url}\n" \
                         f"Headers: {fuzz_headers}\n" \
                         f"Params: {fuzz_params}\n" \
                         f"Data: {fuzz_data}\n" \
                         f"Response Code: {response.status_code}\n" \
                         f"Response Body: {response.text[:100]}...\n" \
                         f"{'-'*60}\n"
            
            print(colored(log_output, 'yellow'))
            
            # Save output to file if requested
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(log_output)
        
        except Exception as e:
            print(colored(f"Error during fuzzing: {e}", 'red'))

# Parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="API Fuzzer Supreme (AFS) - Fuzz your APIs like a boss!")
    
    parser.add_argument("url", help="Target API URL")
    parser.add_argument("-X", "--method", choices=["GET", "POST", "PUT", "DELETE"], default="GET", help="HTTP method to use")
    parser.add_argument("-H", "--headers", nargs='*', help="Custom headers for the request")
    parser.add_argument("-P", "--params", nargs='*', help="Query parameters for the request")
    parser.add_argument("-d", "--data", help="Data to send in the request body (use 'FUZZ' as placeholder for fuzzing)")
    parser.add_argument("-o", "--output", help="File to save the output logs")
    
    return parser.parse_args()

# Main function
def main():
    # Print the banner
    print_banner()
    
    # Parse arguments
    args = parse_arguments()

    # Prepare headers and params as dictionaries
    headers = {header.split(":")[0]: header.split(":")[1] for header in args.headers} if args.headers else None
    params = {param.split("=")[0]: param.split("=")[1] for param in args.params} if args.params else None

    # Logging configuration
    if args.output:
        logging.basicConfig(filename=args.output, level=logging.INFO)

    print(colored(f"Starting API fuzzing on {args.url} using {args.method} method", 'cyan'))
    time.sleep(1)  # Sleep for effect

    # Start fuzzing
    fuzz_api(args.url, args.method, headers, params, args.data, args.output)

if __name__ == "__main__":
    main()
