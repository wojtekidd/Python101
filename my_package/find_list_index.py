import random

print(random.__file__)

def index_number(a_list, elem):
    return a_list.index(elem)
    # idx = 0
    # for item in a_list:
    #     if item == elem:
    #        return idx
    #     idx += 1
    #
    # return None


def random_elem(alist):
    return random.choice(alist)

if __name__ == "__main__":
    print("This is find_list_index module")

"""Add error handling"""

print(index_number([1,2,3,4], 4))
print(random_elem([1,2,3,4]))
