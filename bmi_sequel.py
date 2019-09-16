def compute_bmi(weight, height):
    return round(weight / (height**2), 2)


user_weight = float(input("Your weight (in kg): "))
user_height = float(input("Your height (in m): "))

bmi = compute_bmi(user_weight, user_height)

print(f"Your bmi is {bmi}")

if bmi >= 25:
    print("Go and run")
elif bmi <= 18.5:
    print("Go eat something")
else:
    print("Everything is fine")
