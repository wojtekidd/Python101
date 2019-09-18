from random import randint

user_number = int(input("Give me a number from 1 to 10: "))
comp_number = randint(1,10)

while True:
    if user_number == comp_number:
        print("You win!")
    else:
        print(f"You loose! Computer has chosen {comp_number}")
    break

