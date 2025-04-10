import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as error:
        return error

def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if a == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError as error:
        return error

def logarithm(a, b):
    try:
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError
        return math.log(a, b)
    except ValueError as error:
        return error
def exponent(a, b):
    return a**b



