x = int(input("Give me a number: "))
x_is_not_one = True

while x_is_not_one:
    if x%2 == 0:
        x /= 2
    else:
        x = x*3+1
    print(x)
    if x ==1:
        break
