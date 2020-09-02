from typing import Union


# task 1
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp <= 0:
        raise ValueError('This function works only with exp > 0')
    elif exp == 1:
        return x
    else:
        return x * to_power(x, exp-1)


#task 2
def is_palindrome(string: str) -> bool:
    if len(string)<=1:
        return True
    elif string[0] == string[-1]:
        return(is_palindrome(string[1:-1]))
    else:
        return False


# task 3
def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError('This function works only with postive integers')
    elif n == 1:
        return a
    elif n == 0:
        return 0
    else:
        return a + mult(a, n-1)


# task 4
def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:-1])


if __name__ == '__main__':
    print(to_power(0, 3))
    print(is_palindrome('sassas'))
    print(mult(90, 1))
    print(reverse('Jam'))
