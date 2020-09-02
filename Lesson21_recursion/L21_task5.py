import argparse

def sum_of_digits(digit_string: str) -> int:
    try:
        if len(digit_string) == 1:
            return int(digit_string[0])
        else:
            sum = int(digit_string[0]) + sum_of_digits(digit_string[1:])
            return sum_of_digits(str(sum))
    except ValueError:
        print('ValueError("input string must be digit string")')


def date_to_digit(date: str) -> str:
    return ''.join(filter(str.isdigit, date))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check your lucky number')
    parser.add_argument('birth_date', help='Date of birth in format 05/04/1995')
    args = parser.parse_args()

    print(f'Birhday: {args.birth_date}')
    converted_input = date_to_digit(args.birth_date)
    print(f'Your lucky number is {sum_of_digits(converted_input)}')
