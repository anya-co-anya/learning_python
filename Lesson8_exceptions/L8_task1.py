# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError('oops_Error')

def function_for_error():
    try:
        oops()
    except Exception as error:
        print(error)

function_for_error()