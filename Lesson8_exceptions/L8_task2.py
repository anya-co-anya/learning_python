# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,

# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def get_count_two_numbers():
    a = input('Please enter first number ').strip()
    b = input('Please enter second number ').strip()
    try:
        a = int(a)
        b = int(b)
        return a**2/b
    except ValueError:
        print(f'{a} and/or {b} are not numbers ')
        return 0
    except ZeroDivisionError:
        print('Cannot divide by zero')
        return 0

print(get_count_two_numbers())
