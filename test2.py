# Script computes the area of the circle with the given radius 'r'.
from math import pi

raw_r = input("❔ Input the length of the radius:️ ")
r = float(raw_r)
area = pi * r ** 2
rounded_area = round(area, 3)
print("⚪️ The area of the circle is:", rounded_area, sep=" ", end="\n")
