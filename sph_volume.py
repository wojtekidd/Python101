from math import pi
r = int(input("Give me an R: "))
volume = 4/3 * pi * r**3

while True:
    if 1 <= r <= 1000:
        print(volume)
    else:
        print("R is either less than zero or more than 1000")
    break
