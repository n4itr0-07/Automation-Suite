# MD5 Hash Cracker

Welcome to **MD5 Hash Cracker by NAITRO 07**! This tool is designed to help security enthusiasts and ethical hackers crack MD5 hashes using a wordlist. The script tries each word in a given wordlist, hashing it with MD5, and checks if it matches the hash you want to crack. 

## Features

- **Simple to Use**: Just provide a wordlist and an MD5 hash to be cracked.
- **Real-Time Feedback**: See which passwords are being tried, with colorful output for an engaging experience.
- **Error Handling**: If there’s an issue with the wordlist, the tool lets you know.

---

## Setup and Requirements

### Prerequisites
- **Python 3.x**: Make sure Python is installed on your system.
- **Colorama**: This library is used for colorful terminal output. Install it with:
  
  ```bash
  pip install colorama
  ```

### Files Required
- **`script.py`**: The main script file.
- **`wordlist.txt`**: A text file containing a list of possible passwords, one per line.

---

## Usage

1. **Prepare the Wordlist**:
   - Create or download a `wordlist.txt` file with potential passwords, each on a new line. You can use common password lists or create your own.

2. **Run the Script**:
   - Open a terminal in the directory where `script.py` is located.
   - Run the following command, replacing `<your-wordlist-path>` with the path to your `wordlist.txt` and `<md5-hash>` with the hash you want to crack:

     ```bash
     python script.py
     ```

3. **Follow the Prompts**:
   - Enter the wordlist file location (e.g., `C:\path\to\wordlist.txt` or just `wordlist.txt` if it’s in the same directory as the script).
   - Enter the MD5 hash you want to crack (e.g., `482c811da5d5b4bc6d497ffa98491e38` for "password123").

4. **Wait for the Result**:
   - If the script finds a matching password, it will display it in green with a success message.
   - If it doesn’t find the password in the wordlist, it will inform you that the password wasn’t found.

---

## Example Output

Here’s an example of what the output might look like when you run the script:

```plaintext
==============================================
       MD5 Hash Cracker by NAITRO 07
==============================================

Enter wordlist file location: wordlist.txt
Enter MD5 hash to be cracked: 482c811da5d5b4bc6d497ffa98491e38

Trying password: password123
Trying password: 12345678
Trying password: qwerty
Trying password: password1
...
[+] Found cleartext password: password123
```

If the password is not found in the wordlist, you’ll see this message:

```plaintext
[-] Password not found in wordlist.
```

---

## Troubleshooting

- **File Not Found Error**: Ensure the path to `wordlist.txt` is correct. Use an absolute path if necessary, like `C:\path\to\wordlist.txt`.
- **No Match Found**: If the password isn’t found, try a larger wordlist or different wordlist sources for better coverage.

---

## Notes

- **Legal Notice**: Use this tool only for ethical purposes, such as testing your own systems or during authorized security assessments.
- **Performance**: This tool works well with small to medium wordlists. For very large lists, it may take longer to complete.

---

This README should help anyone understand how to use your MD5 hash cracker effectively. Happy cracking! 😊