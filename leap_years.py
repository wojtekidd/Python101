import calendar

def num_of_leap_years(n):

    if n > 2019:
        for element in list(range(2019, n)):
            return (calendar.isleap(element))
    elif n < 2019:
        for element in list(range(n, 2019)):
            return (calendar.isleap(element))
    else: print("2019 is 2019")

print(num_of_leap_years(2013))

"""
Kiedy mamy już funkcję sprawdzającą czy dany rok jest przestępny, to:
- ustawiamy licznik na 0
- robimy pętlę od podanego roku do roku 2019 i w tej pętli sprawdzamy po kolei każdy rok, czy jest przestepny. Jeżeli jest zwiększamy licznik o 1.
- na koniec zwracamy wartość licznika
"""
