'''
Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
'''
from collections.abc import Iterable

class Iterable_custom:
    def __init__(self, data):
        if isinstance(data, Iterable):
            self.data = data
        else:
            self.data = str(data)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data)-1:
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index]

    def __getitem__(self, item):
        return self.data[item]


if __name__ == '__main__':
    my_str = Iterable_custom(2.0)
    for i in my_str:
        print(i)

    print()

    print(f'3d element: {my_str[2]}')