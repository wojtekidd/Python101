number = int(input("Give me a number: "))

if number % 7 == 0 or number % 5 == 0 or number % 3 == 0:
    print(f"Number {number} is divisible by 7 or 5 or 3")
if number % 7 == 0 and number % 5 == 0:
    print(f"Number {number} is divisible by 7 and 5")
if number % 5 == 0 and number % 3 == 0:
    print(f"Number {number} is divisible by 5 and 3")
if number % 3 == 0 and number % 7 == 0:
    print(f"Number {number} is divisible by 7 and 3")
if number % 7 != 0 and number % 5 != 0 and number % 3 != 0:
    print(f"Number {number} isn't divisible by 7 nor 5 nor 3")
