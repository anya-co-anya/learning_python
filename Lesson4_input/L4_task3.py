import random

HOW_MANY_TIMES_TO_PRINT = 5  # add a number of how many times to shuffle and print text
already_printed_count = 0

input_str = input('Let`s play. Please enter your text:\n')

while already_printed_count < HOW_MANY_TIMES_TO_PRINT:
    print(''.join(random.sample(input_str, len(input_str))))
    already_printed_count += 1