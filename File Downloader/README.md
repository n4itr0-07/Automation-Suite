# File Downloader by NAITRO 07

## Overview

**File Downloader by NAITRO 07** is a Python script that allows you to download files directly from URLs you input. This tool is interactive, letting you add multiple URLs, choose filenames for each download, and receive real-time feedback on each file’s download status. It’s a simple and handy way to gather files from various sources all at once!

---

## Features

- **Interactive Input**: Enter URLs and filenames as you go, adding as many files as you need.
- **User-Friendly Feedback**: Color-coded messages make it easy to follow each download's progress.
- **Customizable Filenames**: Name each file exactly as you want it saved.

---

## Requirements

- **Python 3**
- **Colorama** library for colorful terminal output.

Install Colorama by running:
```bash
pip install colorama
```

---

## How It Works

When you run the script, it will prompt you to:
1. **Enter the URL** of the file you want to download.
2. **Enter a filename** to save the file as, including the extension (e.g., `myfile.png` or `report.pdf`).
3. Choose whether to **add more files** by typing `yes` or `no`. You can add as many files as you need.

Once you’ve entered all your files, the script will download each one, providing a **success** message if it downloads successfully or an **error** message if something goes wrong.

---

## Usage

To start the script, run:

```bash
python file_downloader.py
```

### Example Interaction

Here’s an example of how an interaction with the script might look:

```plaintext
==============================================
          File Downloader by NAITRO 07        
==============================================

Enter the URL of the file to download: https://assets.tryhackme.com/img/THMlogo.png
Enter the filename to save as (with extension): THMlogo.png
Would you like to add another file? (yes/no): yes

Enter the URL of the file to download: https://download.sysinternals.com/files/PSTools.zip
Enter the filename to save as (with extension): PSTools.zip
Would you like to add another file? (yes/no): no

[~] Starting download: THMlogo.png from https://assets.tryhackme.com/img/THMlogo.png
[+] Download complete: THMlogo.png

[~] Starting download: PSTools.zip from https://download.sysinternals.com/files/PSTools.zip
[+] Download complete: PSTools.zip

All downloads complete! - Powered by NAITRO 07
```

---

### Notes

- Make sure each URL you enter is valid and points to a downloadable file. An incorrect URL may result in an error.
- You can add as many files as you need in one run.

---

Enjoy using this handy downloader!