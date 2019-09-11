# DRY FTW function - side effect, no values on input nor output
def message():
    print("Line 1")
    print("Line 2")
    print("Line 3")
    print("Line 4")

message()

# Function prints out but doesn't return the value
def square(x):
    result = x ** 2
    print(result)
# Function returns the value
def get_square(x):
    """Return square of the given number."""
    result = x ** 2
    return result

res = get_square(3)
print(res)


