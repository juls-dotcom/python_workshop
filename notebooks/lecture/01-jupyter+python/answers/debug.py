# Did you find the following mistakes?
# - the function 'even' returns True when the number is odd, so has to be reversed
# - the parameter 'numbers' from the function 'foo' has a mutable default value
# - the loop modifies the list while iterating
# 
# The code could look as follows:

def even(num):
    return num % 2 == 0

def foo(numbers=None):
    result = []
    if numbers:
        for number in numbers:
            if not even(number):
                result.append(number)
        result.append(len(numbers))
    return result