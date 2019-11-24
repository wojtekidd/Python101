my_list = ["A", "B", "C", "D"]


def queue(list_name, val):
    list_name.pop()
    list_name.insert(0, val)
    return

print(my_list)
queue(my_list, "E")
print(my_list)

# def stack(list_name, val):



