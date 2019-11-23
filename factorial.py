def fact(n):
    mul = 1
    for i in range(1,n+1):
        mul = mul * i
    return mul


def fact2(n):
    if n == 1:
        return 1
    else:
        return n*fact2(n-1)


print(fact(1000))