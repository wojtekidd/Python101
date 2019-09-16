from random import randint

my_choice = int(input("1. 💎 2. ✂️ 3. 🧻: "))
comp_choice = randint(1,3)

while True:
    if my_choice > 3 or my_choice < 1:
        print("Wrong choice")
        my_choice = int(input("1. 💎 2. ✂️ 3. 🧻: "))
    else:
        break

print(f"Computer chose {comp_choice}")

if my_choice == comp_choice:
    print("It's a tie!")
elif ((my_choice == 1 and comp_choice == 2) or
      (my_choice == 2 and comp_choice == 3) or
      (my_choice == 3 and comp_choice == 1)):
    print("You win 🎉")
else:
    print("You loose 😭")
