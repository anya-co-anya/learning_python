# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
import functools


def stop_words(words: list):
    def decorator_stop_words(func):

        @functools.wraps(func)
        def wrapper_stop_words(*args, **kwargs):
            ret_str = func(*args, *kwargs)
            for word in words:
                ret_str = ret_str.replace(word, '*')
            return ret_str

        return wrapper_stop_words
    return decorator_stop_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    print(create_slogan("Steve"))
