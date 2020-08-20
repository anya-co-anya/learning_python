# Write a decorator `arg_rules` that validates arguments passed to the function.

# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
import functools


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator_arg_rules(func):

        @functools.wraps(func)
        def wrapper_arg_rules(*args):
            args_valid = True

            for arg in args:   # check if args are valid
                if type(arg) != type_:   # check type
                    args_valid = False
                    print(f'Argument {arg} type isn`t supported. Must be {type_.__name__}.')
                    break
                if len(str(arg)) > max_length:  # check lenght
                    args_valid = False
                    print(f'Argument {arg} is too long. Must be less than {max_length}.')
                for item in contains: # check prohibited symbols
                    if item not in str(arg):
                        args_valid = False
                        print(f'Argument {arg} doesn`t contain required symbol {item}')

            if args_valid:
                return func(*args)
            else:
                return False

        return wrapper_arg_rules
    return decorator_arg_rules


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan('johndoe05@gmail.com'))
    print(create_slogan('S@SH05'))
