# This will create on elist with many values
# def my_func(value, my_list=[]):
#     my_list.append(value)
#     return  my_list

def my_func(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list

print(my_func(value=10)) #10
print(my_func(value=20)) #20
print(my_func(value=20)) #20
"""
List object is modified but stays in the same place in memory
"""