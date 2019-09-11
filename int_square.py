# Ask for an integer and print its square.
number = int(input("Input an integer number: "))

result = number ** 2
# Default formatting
print(number, "squared equals:", result)
# f-string formatting
print(f"{number} squared equals: {result}")

