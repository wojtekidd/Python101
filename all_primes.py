import is_prime


def all_primes(n):
    for element in range(0, n):
        if is_prime(element) is True:
            return element


print(all_primes(20))
