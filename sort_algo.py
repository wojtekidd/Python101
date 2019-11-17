tab = [98, 100, 99, 2, 45, 101, 105, 1]
"""Selection sort"""
def sort_array(array):
    for counter in range(len(array)):
        min_el = array[counter]
        min_ind = counter
        for iterator in range(counter, len(tab)):
            if min_el > tab[iterator]:
                min_el = tab[iterator]
                min_ind = iterator
            print(f"step: {counter}, min_index: {min_ind}, min_element: {min_el}, iterator: {iterator}, array:{array}")
        tab[min_ind] = tab[counter]
        tab[counter] = min_el
    return array

print(sort_array(tab))