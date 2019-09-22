list_1 = [1, 2, 43, 5, 10, 7]
sum_1 = 0

for item in list_1:
    print(item)

for item in list_1:
    sum_1 += item

print(sum_1)


iterator = 0
sum_1 = 0
list_length = len(list_1)

while iterator < list_length:

    sum_1 += list_1[iterator]

    iterator += 1

print(sum_1)
"""As above so below"""
print(sum(list_1))

for item in list_1:
    print(item)


