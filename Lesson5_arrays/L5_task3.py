original_list = list(range(1, 101))
final_list = []

x = 0
while x < len(original_list):
    if original_list[x] % 7 == 0 and original_list[x] % 5 != 0:
        final_list.append(original_list[x])
    x += 1


print(f'Numbers from 1 to 100 that are divisible by 7 but not a multiple of 5:\n{final_list}')

#  alternative

new_list = [i for i in list(range(1, 101)) if i % 7 == 0 and i % 5 != 0]
print(new_list)