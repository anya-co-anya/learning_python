'''Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.'''
import re

class User:
    def __init__(self, email):
        if self.__class__.validate_email(email):
            self.email = email
        else:
            self.email = ''
            print('Invalid email')

    @classmethod
    def validate_email(cls, email: str):
        email = email.lower()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            return True
        else:
            return False


if __name__ == '__main__':
    while 1:
        input_email = input('Enter your email: ')
        if input_email in ('q', 'Q'):
            break
        print(User.validate_email(input_email))