my_list = [1, 2, 3, 4]

# for item in my_list:
#     print(item)

my_iterator = iter(my_list)
while True:
    try:
        item = next(my_iterator)
        print(item)
    except StopIteration:
        break

print(iter(my_iterator))

