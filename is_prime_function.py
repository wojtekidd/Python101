def is_prime(x):
    if x % x == 0 and x / 1 == x:
        return True
    elif x % 2 == 0:
        return False

print(is_prime(19))
print(is_prime(20))

