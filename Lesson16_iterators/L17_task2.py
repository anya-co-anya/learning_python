'''
Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
'''
import itertools

def in_range(start, end, step=1):
    if step == 0:
        raise ValueError('in_range() arg 3 must not be zero')

    current = start
    while (current >= end and step < 0) or (current <= end and step > 0):
            yield current
            current += step


if __name__ == '__main__':
    for i in in_range(-20, 22, 10):
        print(i)
