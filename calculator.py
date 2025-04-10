import math


# First example
import math

def add(a, b): 
    return a + b

def sub(a,b):
    return a-b

def mul(a,b):
    return a * b

def div(a,b):
    try:
        if  a == 0:
            raise ZeroDivisionError
        return b/a

    except ZeroDivisionError as e:
        return e

def log(a,b):
    try:
        if a<=0 or a==1 or b <=0:
            raise ValueError

        return math.log(b,a)


    except ValueError as e:
        return

def exp(a,b):

    return a**b






def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    try:
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError
        return math.log(a, b)
    except ValueError as error:
        print(error)
def exponent(a, b):
    return a**b



