user_name = 'james'

def ask_for_name():
    return input('Please enter your name:\n').lower()

def checkName(name):
    return user_name == name

print(f'Login successful: {checkName(ask_for_name())}')
