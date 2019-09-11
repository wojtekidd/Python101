"""Importing two selected functions from 'functions.py'."""
from functions import exponent, sub

"""Creating custom equation."""
def equation(x, y):
    return exponent(sub(x, y), 3)

print(equation(2, 4))



