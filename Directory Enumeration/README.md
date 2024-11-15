Here’s a README for your interactive Directory Enumerator script that provides clear instructions, usage examples, and expected output in a natural, user-friendly style.

---

# Directory Enumerator by NAITRO 07

## Overview

**Directory Enumerator by NAITRO 07** is a Python script designed to help you find accessible directories on a web server by appending common directory names to a base URL. It uses a wordlist to check each possible directory and displays the results in a color-coded format for easy readability. This tool is useful for penetration testers, web security researchers, and anyone exploring the structure of a web application.

---

## Features

- **Interactive & User-Friendly**: The script displays status updates, uses color-coded output, and provides helpful error messages.
- **Customizable Wordlist**: Use your own list of directory names by editing `wordlist.txt`.
- **Visual Styling**: Output colors make it easy to distinguish between valid and invalid directories.

---

## Requirements

- Python 3
- `colorama` package for colored terminal output

You can install the `colorama` package using:
```bash
pip install colorama
```

---

## How It Works

The script takes a **target domain** as a command-line argument and reads a list of possible directory names from `wordlist.txt`. For each directory in the wordlist, it appends it to the base URL and checks if the directory exists by sending a GET request. If the directory is found, it’s displayed as a valid directory; if not, it’s shown as not found.

### Example Wordlist (`wordlist.txt`)

Here’s a sample `wordlist.txt`:
```plaintext
admin
login
dashboard
uploads
profile
about
contact
```

---

## Usage

1. **Prepare your wordlist**: Add directory names (one per line) to `wordlist.txt`.
2. **Run the script**: Specify the target domain as a command-line argument.

```bash
python directory_enum.py example.com
```

### Example

With the following sample entries in `wordlist.txt`:
```plaintext
admin
login
dashboard
test
```

Running:
```bash
python directory_enum.py example.com
```

### Expected Output

The output will look like this:

```plaintext
============================================
       Directory Enumerator by NAITRO 07    
============================================

Target Domain: example.com
Starting Directory Enumeration...

[-] Not Found: http://example.com/admin.html
[+] Valid Directory: http://example.com/login.html
[-] Not Found: http://example.com/dashboard.html
[-] Not Found: http://example.com/test.html

Scan Complete! - Crafted by NAITRO 07
```

- **Valid directories** will be shown in green with `[+]` for easy identification.
- **Not found directories** will be shown in red with `[-]` to indicate they’re missing.
- A **final message** in cyan will indicate the scan is complete.

---

## Notes

- The script currently assumes an `.html` suffix for each directory. You can modify this in the code if you need a different extension or no extension.
- Ensure that the target server allows directory enumeration to avoid potential issues like IP blocking.

---

Enjoy exploring your target directories safely and effectively!

---