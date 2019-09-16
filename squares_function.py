def squares():
    """"""
    x = 1
    result = ""
    while x<11:
        result = result + str(x**2) + " "
        x += 1
    return result

print(squares())