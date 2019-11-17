t = [4, 5, 6, 2, 22, 46, 34, 78, 9, 10]


# def find_max(array):
#     x = 0
#     i = array[0]
#     for i in range(len(array)):
#         if x < array[i]:
#             x = array[i]
#     return x
#
# print(find_max(t))
#
#
# for counter in range(len(t)):
#     for i in range(len(t)-1):
#         if t[i] > t[i+1]:
#            temp = t[i]
#            t[i] = t[i+1]
#            t[i+1] = temp
# print(t)

def bubble_sort(array):
    for counter in range(len(array)):
        for iterator in range(len(array) - 1):
            if array[iterator] > array[iterator + 1]:
                temp = array[iterator]
                array[iterator] = array[iterator + 1]
                array[iterator + 1] = temp
    return array

print(bubble_sort([1,2,56,8,33]))

element = 22
for i in range(len(t)-1):
    if t[i] == element:
        print(i)