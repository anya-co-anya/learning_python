'''
Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
'''

def with_index(iterable='', start=0):
    for i in iterable:
        yield start, i
        start += 1



if __name__ == '__main__':
    my_str = 'Hey'
    cars = ['kia', 'audi', 'bmw']
    
    print(list(with_index(cars, -10)))

    for i, e in with_index(my_str, 50):
        print(f'{i}: {e}')
