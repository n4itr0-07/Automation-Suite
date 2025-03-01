import random
from math import gcd
from sympy import mod_inverse
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Banner
def banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "    RSA Encryption & Decryption Tool")
    print(Fore.MAGENTA + "        Created by: N4ITR0 07")
    print(Fore.CYAN + "=" * 50 + "\n")

# Step 1: Choose two large prime numbers
def get_prime_input():
    while True:
        try:
            p = int(input(Fore.GREEN + "Enter first prime number (p): "))
            q = int(input(Fore.GREEN + "Enter second prime number (q): "))
            if p != q and p > 1 and q > 1:
                return p, q
            print(Fore.RED + "Both must be prime and different!")
        except ValueError:
            print(Fore.RED + "Invalid input! Enter valid numbers.")

# Step 2: Calculate n and phi(n)
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    def find_e(phi):
        e = random.randrange(2, phi)
        while gcd(e, phi) != 1:
            e = random.randrange(2, phi)
        return e

    e = find_e(phi)
    d = mod_inverse(e, phi)
    return e, d, n

# Encryption
def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

# Decryption
def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main Menu
def main():
    banner()
    p, q = get_prime_input()
    e, d, n = generate_keys(p, q)

    print(Fore.CYAN + "\nGenerated Keys:")
    print(Fore.YELLOW + f"Public Key: (e={e}, n={n})")
    print(Fore.MAGENTA + f"Private Key: (d={d}, n={n})\n")

    while True:
        print(Fore.BLUE + "Options:")
        print(Fore.CYAN + "1. Encrypt a message")
        print(Fore.CYAN + "2. Decrypt a message")
        print(Fore.CYAN + "3. Exit")
        choice = input(Fore.GREEN + "Enter choice: ")

        if choice == '1':
            message = input(Fore.YELLOW + "Enter message to encrypt: ")
            ciphertext = encrypt(message, e, n)
            print(Fore.MAGENTA + f"Ciphertext: {ciphertext}\n")
        elif choice == '2':
            try:
                ciphertext = list(map(int, input(Fore.YELLOW + "Enter ciphertext (comma-separated): ").split(',')))
                decrypted_message = decrypt(ciphertext, d, n)
                print(Fore.MAGENTA + f"Decrypted Message: {decrypted_message}\n")
            except:
                print(Fore.RED + "Invalid ciphertext format!\n")
        elif choice == '3':
            print(Fore.RED + "Exiting...\n")
            break
        else:
            print(Fore.RED + "Invalid choice!\n")

if __name__ == "__main__":
    main()
