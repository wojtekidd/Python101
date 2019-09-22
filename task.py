def func(a, z, *args):
    print(args)
    a_sum = 0
    for item in args:
        a_sum += item
    return a_sum

"""
args take all undefined elements, so here we don't get 2 and 3 displayed
"""

print(func(2, 3, 4, 5, 6, 4233))