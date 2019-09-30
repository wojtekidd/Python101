import is_prime


def all_primes(n):
    for element in range(0, n):
        if is_prime(element) is True:
            return element


print(all_primes(20))

"""
W drugim zadaniu napisz najpierw funkcję, która sprawdza czy podana liczba jest pierwsza (is_prime(n)). 
Do napisania tej funkcji będzie potrzbna pętla, która iteruje po kolejnych liczbach całkowitych (od 1 do n/2). 
Jeżeli nasza liczba n będzie podzielna przez którąś z tych liczb wtedy n nie jest pierwsza. 
Jeżeli liczba n nie będzie podzielna przez żadną z liczb od 1 do n/2 wtedy jest pierwsza.
"""