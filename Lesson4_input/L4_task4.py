import random


operators_list = ('+', '-', '*')
result = None


while 1:
    a = random.randint(1, 100)  # range of numbers. The higher -  the more complicated
    b = random.randint(1, 10)

    operator = operators_list[random.randint(0, len(operators_list)-1)]
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    else:
        print(f'Invalid operator "{operator}"')
        break

    #  get answer from the user
    if result is not None:
        user_answer = input(f'Enter "q" to quit.\n {a} {operator} {b} = ')

        if user_answer.lower() == 'q':
            break

        user_answer = int(user_answer)
        if user_answer == result:
            print('Good job.')
        else:
            print(f'No, it is {result}. Try again.')


