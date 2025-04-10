#https://github.com/Antonezzz/lab10-AZ-EC
#Partner 1: Anthony Zheng
#Partner 2: Edgar Canaan
import math

def square_root(a):
    try:
        if not isinstance(a, (int, float)):
            raise ValueError
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as error:
        raise

def hypotenuse(a, b):
    return math.hypot(a,b)

# First example
import math

def add(a, b): 
    return a + b


def mul(a,b):
    return a * b
def div(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers")
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return b / a
    except ZeroDivisionError:
        raise

def exp(a,b):

    return a**b

def subtract(a, b):
    return a - b


def logarithm(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numeric")
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithm input")
    return math.log(a, b)




