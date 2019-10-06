def div(a, b):
    assert b != 0, "Cannot divide by 0"
    return a/b

    # try:
    #     return a/b
    # except ZeroDivisionError:
    #     print("Cannot divide by 0")

print(div(3,0))

