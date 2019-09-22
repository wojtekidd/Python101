def func(a, z, *args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    a_sum = 0
    for item in args:
        a_sum += item
    return a_sum


"""
args take all undefined elements, so here we don't get 2 and 3 displayed
kwargs display all other arguments
"""

print(func(2, 3, 4, 5, 6, 4233, v=34, s=43))
