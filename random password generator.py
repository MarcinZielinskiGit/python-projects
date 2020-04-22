import secrets
import string


def getpasswd(lenght):
    return "".join((secrets.choice(string.ascii_letters + string.digits + string.punctuation)) for x in range(length))


length = int(
    input('How many characters would you like your password to have: '))

print('Your password has benn generated: ', getpasswd(length))
