# **EmailEnum - Email Enumeration Script**

This script helps identify valid email addresses from a list by interacting with a login page on a target website. It checks whether an email is valid based on the response received from the website’s login function.

## **How It Works**
The script sends a login request with each email from the provided list, using a dummy password. Based on the server's response, the script determines whether the email exists in the system or not.

### **Features:**
- Automated email enumeration using POST requests.
- Identifies valid and invalid email addresses based on the server's response.
- Can be used for login page enumeration and brute-force attacks.
---  
### Bulk Emails
```
https://github.com/nyxgeek/username-lists/blob/master/usernames-top100/usernames_gmail.com.txt
```
## **Usage**

### **1. Prerequisites**
- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

### **2. Running the Script**

To use the script, provide a file containing a list of email addresses (one per line):

```bash
python3 script.py <email_list_file>
```

Example:

```bash
python3 script.py emails.txt
```

### **3. Output**
The script will output valid and invalid email addresses to the terminal. Valid emails will also be stored in a list, which can be further used for reporting or exploitation.

Example output:

```bash
[INVALID] user1@example.com
[VALID]   admin@example.com
[VALID]   user2@example.com
```

### **4. Script Logic**
The script sends a POST request with the following fields:
- **`username`**: Email address from the list
- **`password`**: A placeholder password (not relevant since we're only checking the validity of emails)
- **`function`**: Login action

If the response indicates the email is invalid, the script prints `[INVALID]`. Otherwise, it prints `[VALID]` for valid emails.

## **Customization**

You can customize the script to work with different websites by modifying:
- **`url`**: Change this to point to the target website's login function.
- **`headers`**: Update to reflect the headers required by the target website.
- **`data`**: Adjust the form fields to match the expected parameters of the login page.

### **5. Example Email List File**
Here’s an example of how the email list file should be formatted:

```
admin@example.com
user1@example.com
user2@example.com
```

## **Disclaimer**
This script is designed for educational purposes and authorized security testing only. Ensure you have explicit permission before using this tool against any website or service.

## **License**
This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

