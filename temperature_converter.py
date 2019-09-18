temperature = float(input("What does the temperature scale say? "))
measure = input("(c)elsius or (f)arenheit? ")

while True:
    if measure == "c":
        print((temperature*2)*(1/10))
    elif measure == "f":
        print(temperature)
    else:
        print("You can either put 'c' or 'f'")
    break
