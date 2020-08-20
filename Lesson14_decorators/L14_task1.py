# Write a decorator that prints a function with arguments passed to it.
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper_logger(*args, **kwargs):
        args_str = ', '.join(str(i) for i in args)
        kwargs_str = ', '.join(f'{k}: {v}' for k, v in kwargs.items())
        print(f'{func.__name__} called with {args_str}; {kwargs_str}:')
        return func(*args, **kwargs)

    return wrapper_logger


@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == '__main__':
    print(add(1, 2))
    print(square_all( 9, 6, 8))