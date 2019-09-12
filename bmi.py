def compute_bmi(x, y):
    return x / (y**2)


x = float(input("Your weight: "))
y = float(input("Your height: "))

bmi = compute_bmi(x, y)
bmi_rounded = round(bmi, 3)
print(bmi_rounded)
