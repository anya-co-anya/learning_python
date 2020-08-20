import random

number_to_guess = random.randint(1, 10)
user_number = None

# get a number
while user_number not in range(1, 11):
    user_number_str = input('Guess a natural number from 1 to 10:\n')
    if user_number_str.isnumeric() is False:
        print('Your "number from 1 to 10" is not a NATURAL NUMBER')
    else:
        user_number = int(user_number_str)
        if user_number not in range(1, 11):
            print('You number is not in range from 1 to 10')


# check the guessing
if user_number == number_to_guess:
    print('Correct!')
else:
    print(f'Not correct. The number is {number_to_guess}')


