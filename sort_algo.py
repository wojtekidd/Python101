tab = [98, 100, 99, 2, 45, 101, 105, 104]

for j in range(len(tab)):
    min_el = tab[j]
    min_ind = j
    for i in range(j, len(tab)):
        if min_el > tab[i]:
            min_el = tab[i]
            min_ind = i
    tab[min_ind] = tab[j]
    tab[j] = min_el

print(tab)