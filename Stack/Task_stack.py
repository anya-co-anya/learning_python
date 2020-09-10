import unittest

class Stack:
    def __init__(self):
        self.__list = []

    def push(self, element):
        self.__list.append(element)

    def get_show(self):
        return self.__list[-1] if self.__list else None

    def get_pop(self):
        if self.get_show():
            return self.__list.pop()
        else:
            return None


class CheckFunctions:

    @staticmethod
    def check_round_brackets(string: str) -> bool:
        stack = Stack()
        for i in string:
            if i == '(':
                stack.push(i)
            elif i == ')':
                if stack.get_show() is None:  # if there are more closing brackets
                    return False
                stack.get_pop()
        return False if stack.get_show() else True

    @staticmethod
    def check_all_brackets(string: str) -> bool:
        stack = Stack()
        opening = ('(', '[', '{')
        closing = (')', ']', '}')

        for i in string:
            if i in opening:
                stack.push(i)
            elif i in closing:
                index = closing.index(i)
                if stack.get_show() == opening[index]:
                    stack.get_pop()
                else:
                    return False

        return False if stack.get_show() else True


class TestStack(unittest.TestCase):
    def test_push(self):
        try:
            self.stack_first.push('test_element')
            self.stack_first.push(15)
            self.stack_first.push([1, 2, 3, 4, 5])
        except:
            self.assertTrue(False, msg='Exception occurred')

    def test_show(self):
        test_a = 'a'
        self.stack_first.push(test_a)
        self.assertIs(self.stack_first.get_show(), test_a, msg = 'different values')
        test_a = 1234
        self.stack_first.push(test_a)
        self.assertIs(self.stack_first.get_show(), test_a, msg='different values')

    def test_pop(self):
        test_a = 'a'
        self.stack_first.push(test_a)
        test_b = self.stack_first.get_pop()
        self.assertIs(test_a, test_b, msg='Get another object')
        self.assertIs(self.stack_first.get_pop(), None, msg='Must be None')


    def setUp(self) -> None:
        self.stack_first = Stack()
        print('setup')


class TestCheckFunctions(unittest.TestCase):
    def test_check_all_brackets(self):
        list_test_true = ['([])', '{[]{()}}']
        list_test_false = ['([)]', '[]}' ')', '{[]','(']
        for i in list_test_true:
            self.assertTrue(CheckFunctions.check_all_brackets(i), f'Returns False for {i}')
        for i in list_test_false:
            self.assertFalse(CheckFunctions.check_all_brackets(i), f'Returns True for {i}')


if __name__ == '__main__':
    # unittest.main()
    a = input('Expression with round brackets: ')
    b = input('Expression with different brackets: ')
    print(f'Is {a} valid? -> {CheckFunctions.check_round_brackets(a)}')
    print(f'Is {b} valid? -> {CheckFunctions.check_all_brackets(b)}')