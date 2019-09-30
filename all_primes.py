def all_primes(x):

    def is_prime(n):
        for item in range(1, int(n/2)):
            if n % item == 0:
                return False
        return True

    all_prime_numbers = []
    for element in range(1, n):
        if is_prime(element) is True:
            all_prime_numbers.append(element)






"""
Odnośnie drugiego zadania, kiedy mamy już funkcje is_prime używamy ja wewnątrz drugiej funkcji. 
Ta druga funkcja przechodzi po wszystkich liczbach mniejszych od n i za każdym razem sprawdza czy aktualna liczba jest pierwszą. 
Jeżeli jest pierwsza dodaje ja do wcześniej przygotowanej list. Na koniec zwraca zapełniona listę.
"""