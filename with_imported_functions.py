print("Global namespace before import: ", globals())
import my_functions, sys,my_module
#from my_functions import add, exponent
#import my_functions as mf
print(sys.path)

print(my_functions.add(4,2))
