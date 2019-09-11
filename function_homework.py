def my_function(x):
    result= round(((x ** 0.5) + ((1 - (x ** 2)) ** 0.5)), 3)
    return result


x = float(input("X:"))

res = my_function(x)
print(res)