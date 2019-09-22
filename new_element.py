a = [1, 2, 3, 4, 5]
a.append(6)
a[1] = 0
print(a)

tuple_a = (1, 2, 3, 4)
tuple_b = (5, )
print(tuple_a+tuple_b)

tuple_a += (5, )
print(tuple_a)
