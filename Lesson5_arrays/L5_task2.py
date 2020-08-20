import random

list_1 = []
list_2 = []
LIST_LENGTH = 10  # change length here
RANGE_FOR_RANDOM = (1, 10)  # change the range of random numbers


#  add random integers to the lists
while len(list_1) < LIST_LENGTH:
    list_1.append(random.randint(RANGE_FOR_RANDOM[0], RANGE_FOR_RANDOM[1]))

while len(list_2) < LIST_LENGTH:
    list_2.append(random.randint(RANGE_FOR_RANDOM[0], RANGE_FOR_RANDOM[1]))


#  convert to sets and find common
set_1 = set(list_1)
set_2 = set(list_2)
common_list = list(set_1.intersection(set_2))


#  print result
print(f'Our lists are: \n{list_1}\n{list_2}\n')
print(f'List of common elements is {common_list}')