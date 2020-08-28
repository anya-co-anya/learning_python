'''
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
'''
import itertools

def in_range(start, end, step=1):
    for i in itertools.count(start, step):
        if i >= end:
            break
        yield i


if __name__ == '__main__':
    for i in in_range(0, 10):
        print(i)
