from builder.computer4 import Computer
from builder.my_computer4 import MyComputer

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
