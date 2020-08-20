# A simple calculator.
# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter.
# Then return the sum or product of all the numbers in the arbitrary parameter.

# For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


#  function to make operation
def make_operation(operator):

    def make_plus(args):  # parameter must be a list
        result = 0 + args[0]
        for i in args[1:len(args)+1]:
            result += i
        print(f'Sum operation of you numbers {args} will return {result}')
        return result

    def make_minus(args):
        result = 0 - args[0]
        for i in args[1:len(args)+1]:
            result -= i
        print(f'Subtraction operation of you numbers {args} will return {result}')
        return result

    def make_multiply(args):
        result = args[0]
        for i in args[1:len(args)+1]:
            result *= i
        print(f'Multiplication operation of you numbers {args} will return {result}')
        return result

    if operator == '+':
        return make_plus
    if operator == '-':
        return make_minus
    if operator == '*':
        return make_multiply


#  get operator from user
while 1:
    user_operator = input('Please enter operator: +, -, *: ').strip()
    if user_operator in ['+', '-', '*']:
        break
    else:
        print('Operator in not valid. Please enter one of +, -, *')
        continue


#  get number values from user
print('\nPlease enter at least 2 values.')
user_values = []

while 1:
    new_input = input('Press q if you don`t have any more numbers. Enter a number: ').strip()
    if new_input.lower() == 'q' and len(user_values)>=2:
        break
    try:
        new_input = int(new_input)
    except ValueError:
        print('Your number is not valid.')
        continue
    user_values.append(new_input)


#  run function
x = make_operation(user_operator)
x(user_values)


