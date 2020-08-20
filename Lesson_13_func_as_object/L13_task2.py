# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def actions_with_strings():
    def make_name_format(input_str: str):
        return input_str.strip().lower().capitalize()

    def make_camelcase(input_str: str):
        return ''.join(word.capitalize() for word in input_str.rsplit())

    return make_name_format, make_camelcase


if __name__ == '__main__':
    actions_with_str = actions_with_strings()

    print(actions_with_str[0]('olEh'))
    print(actions_with_str[1]('class name can be here'))



