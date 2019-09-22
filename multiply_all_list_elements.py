list_1 = [1, 2, 3, 4, 5, 6]

mul = 1

for item in list_1:
    mul *= item

print(mul)

"""Robimy silnie (n+1 zeby zero ominac)"""
def factorial(n):
    mul = 1
    for item in range(1, n+1):
        mul *= item
    return mul

print(factorial(5))
