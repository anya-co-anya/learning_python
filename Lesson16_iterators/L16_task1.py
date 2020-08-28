'''
Create your own implementation of a built-in function enumerate, named `with_index`,
which takes two parameters: `iterable` and `start`, default is 0.
'''

def with_index(iterable='', start=0):
    counting_list = [i for i in range(start, start+len(iterable))]
    zip(counting_list, iterable)
    return zip(counting_list, iterable)


if __name__ == '__main__':
    my_str = 'Hey'
    
    print(list(with_index(my_str)))

    for i, e in with_index(my_str, 56):
        print(f'{i}: {e}')
