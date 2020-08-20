import random

#  generate a random list
LIST_LENGTH = 10
list_random_numbers = []

while len(list_random_numbers) < LIST_LENGTH:
    list_random_numbers.append(random.randint(1, 999))

#  get the max number
max_random_number = max(list_random_numbers)

#  print result
print(f'Our random list is: {list_random_numbers}')
print(f'Max number from the list is {max_random_number}')