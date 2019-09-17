first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))
third  = int(input("Give me the third number: "))
sum = first + second + third

while first == second == third:
        print(3*sum)
        break
else:
    print(sum)
