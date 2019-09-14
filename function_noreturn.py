def function():
    print(round((0.5 ** 0.5) + ((1 - (0.5 ** 2)) ** 0.5), 3))


function()

from math import sqrt

def function1():
   result = math.sqrt(0.5) + math.sqrt(1-(0.5)**2)
   rounded_result = round(result, 3)
   print(rounded_result)

function1()