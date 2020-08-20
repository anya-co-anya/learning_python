a = 5
b = 46
operator = '//'  # add operator here; it can be +, -, /, *, **, %, //

result = None

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '/':
    result = a / b
elif operator == '*':
    result = a * b
elif operator == '**':
    result = a ** b
elif operator == '%':
    result = a % b
elif operator == '//':
    result = a // b
else:
    print(f'Invalid operator "{operator}"')

if result is not None:
    print(f'{a} {operator} {b} = {result}')