# Write a Python program to detect the number of local variables declared in a function.

def my_f():
    a = 56
    b = 34
    c = 75

def detect_local_variables(function):
    return function.__code__.co_nlocals

if __name__ == '__main__':
    print(detect_local_variables(my_f))