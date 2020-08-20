phone_number = '9003940939'

if phone_number.isnumeric() and len(phone_number) == 10:
    print(f'Your number {phone_number} has been saved. Thank you.')
else:
    print('Please enter valid number.')


