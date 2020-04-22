
def login():
    while True:
        login_temp = input('Enter your login: ')
        if login_temp in credentials:
            if input('Enter the password: ') == str(credentials[login_temp]):
                logged_in()
                return False
            else:
                print('Incorrect password. Try again.')
        else:
            print('Login doesnt exist. Try again.')

def signin():
    while True:
        new_login = input('Enter your new login: ')
        if new_login in credentials:
            print('This login is taken. Please use another one.')
        else:
            while True:
                new_password = input('Enter you new passowrd: ')
                repeated_password = input('Repeat your password: ')
                if new_password != repeated_password:
                    print('Passwords do not match. Try again.')
                else:
                    credentials[new_login] = new_password
                    print('Credentials saved. Please login.')
                    login()
                    return False

def logged_in():
    print('Welcome back!')

def main():
    login_or_signin = input('Would you like to login or sign in? (L/S) ')
    if login_or_signin == 'l' or login_or_signin == 'L':
        login()
    elif login_or_signin == 's' or login_or_signin == 'S':
        signin()
    else:
        print('Incorrect input.')
        main()

credentials = {
    'marcin' : 1234,
    'tom' : 4321
}

main()
