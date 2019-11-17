# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# print(fib(20))

def fib_iter(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    if n >= 2:
        for i in range(2, n):
            temp = a
            a = b
            b = temp + a
        """f string debugujacy"""
        result = a + b
        return result


print(fib_iter(100))