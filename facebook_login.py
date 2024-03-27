import requests
import getpass

def try_password(username, password):
    login_url = 'https://www.facebook.com/login.php'
    payload = {
        'email': username,
        'pass': password
    }
    session = requests.Session()
    response = session.post(login_url, data=payload)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        print(f'Successful login with password: {password}')
        return True
    else:
        print(f'Failed login with password: {password}')
        return False

def main():
    username = input('Enter your Facebook username/email: ')
    password_list = []
    for i in range(3):
        password = getpass.getpass(f'Enter password attempt {i+1}: ')
        password_list.append(password)
    
    success = False
    for password in password_list:
        if try_password(username, password):
            success = True
            break
    
    if not success:
        print('All password attempts failed.')

if __name__ == '__main__':
    main()
