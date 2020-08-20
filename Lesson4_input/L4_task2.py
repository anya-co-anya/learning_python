# get user name
user_name = input('Please enter you name: ')

# get user age
user_age = None
while 1:
    user_age is None
    try:
        user_age = int(input('How old are you? '))
        if user_age < 0:
            print('Come on. You are not that young :)')
            continue
        else:
            break
    except ValueError:
        print('Please enter age as a natural number')

# print greeting
print(f'Hello {user_name}, on your next birthday you’ll be {user_age+1} years')
