# Subdomain Finder by NAITRO 07

## Overview

This Python script, **Subdomain Finder by NAITRO 07**, scans a list of subdomains to identify valid ones associated with a given main domain. It outputs valid and invalid domains in a color-coded format, making it easy to see which subdomains are accessible.

This tool is handy for anyone looking to enumerate subdomains of a website for security assessments or research purposes.

---

## Features

- **Color-coded output** for quick identification of valid and invalid domains.
- **Smooth output effect** using small delays for a visually appealing experience.
- **Customizable** - add your own list of subdomains to scan by modifying `subdomains.txt`.

---

## Requirements

- Python 3
- `colorama` package for colorful terminal output

Install `colorama` by running:
```bash
pip install colorama
```

---

## How It Works

The script reads subdomains from a file (`subdomains.txt`) and attempts to connect to each one by appending it to the main domain provided as a command-line argument. If the connection is successful, the domain is valid and will be printed in **green**. If not, the domain will be printed in **red** as invalid.

### File Structure

- **`subdomains.txt`** - A text file where each line contains a subdomain to scan.
- **`subdomain_finder.py`** - The main Python script to run.

### Example `subdomains.txt` Contents
```plaintext
www
blog
shop
mail
dev
```

---

## Usage

1. **Prepare the subdomains list**: Add subdomains in `subdomains.txt`, one per line.
2. **Run the script**: Execute the script with the target domain as an argument.

```bash
python subdomain_finder.py example.com
```

### Example

Let's say you have `subdomains.txt` with the following entries:
```plaintext
www
mail
blog
test
```

Running:
```bash
python subdomain_finder.py example.com
```

### Expected Output

The output will look like this:

```plaintext
============================================
        Subdomain Finder by NAITRO 07       
============================================

[+] Valid domain found: http://www.example.com
[-] Invalid domain: http://mail.example.com
[+] Valid domain found: http://blog.example.com
[-] Invalid domain: http://test.example.com

Scan Complete! - Crafted by NAITRO 07
```
![Screenshot 2024-11-15 110616](https://github.com/user-attachments/assets/2762e3f5-96ba-4123-9aa7-14119c79c197)


- **Valid domains** appear in green.
- **Invalid domains** appear in red.
- Final message in **magenta** signals the end of the scan.

---

## Notes

- This script currently only supports HTTP. Modify the `sub_domains` line in the code to use HTTPS if needed.
- Feel free to experiment with different subdomain lists to explore other possible endpoints for your target domain.

---

Enjoy the scan and stay safe!

---
