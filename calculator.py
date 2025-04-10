import math

<<<<<<< HEAD
=======
def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as error:
        return error

def hypotenuse(a, b):
    return math.hypot(a,b)
>>>>>>> 63902e42977b540e2aba4ac00f6bcabf98c7df02

# First example
import math

def add(a, b): 
    return a + b


def mul(a,b):
    return a * b

def div(a,b):
    try:
        if  a == 0:
            raise ZeroDivisionError
        return b/a

    except ZeroDivisionError as e:
        return e

def exp(a,b):

    return a**b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    try:
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError
        return math.log(a, b)
    except ValueError as error:
        return error




