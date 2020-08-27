''' Write a class TypeDecorators
which has several methods for converting results of functions to a specified type (if it's possible) '''
import functools

class TypeDecorators:
    @staticmethod
    def to_int(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            try:
                return int(ret)
            except ValueError:
                print(f'Cannot convert {ret} to int.')
                return ret

        return wrapper

    @staticmethod
    def to_str(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_bool(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func(*args, **kwargs):
                return True
            else:
                return False

        return wrapper

    @staticmethod
    def to_float(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            try:
                return float(ret)
            except ValueError:
                print(f'Cannot convert {ret} to float.')
                return ret

        return wrapper



@TypeDecorators.to_str
def calculate(a: int, b: int):
    return a + b

@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


if __name__ == '__main__':
    print(calculate(5, 6), type(calculate(5, 6)))
    print(do_nothing('25'), type(do_nothing('25')))
    print(do_something('True'), type(do_something('True')))