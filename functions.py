"""Module with my functions"""


def add(x, y):
    """Return sum of two numbers."""
    return x + y


def sub(x, y):
    """Return difference of two numbers."""
    return x - y


def mul(x, y):
    """Return product of two numbers."""
    return x * y


def div(x, y):
    """Return quotient of two numbers."""
    return x // y
    print("I'm after `return`")


def exponent(x, y):
    """Return first given number to the power of second given number."""
    return x ** y


def square(x):
    """Return square of the given number."""
    return exponent(x, 2)


def custom_equation(x, y):
    """Custom equation."""
    return add(div(square(add(x, y)), sub(x, 5)), mul(3, y))
