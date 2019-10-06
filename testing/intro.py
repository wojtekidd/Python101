def kw(a, b):
    return (a + b) ** 2

def factorial(n):
    if n <= 0:
        return None
    res = 1
    for num in range(1, n+1):
        res *= num
    return res

print("Running kw tests:")
assert kw(4, 2) == 36, "Failed"
print("1st test passed ✅")
assert kw(5, 2) == 49, "Failed"
print("2nd test passed ✅")
assert kw(8, -2) == 36, "Failed"
print("3rd test passed ✅")

print("Running factorial tests:")
assert factorial(5) == 120, "Failed"
print("1st test passed ✅")

# if div(4, 2) == 2:
#     print("Passed")
# else:
#     raise Exception("Failed")

print("All test passed")
