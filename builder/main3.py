from builder.computer3 import Computer
from builder.my_computer import MyComputer

builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()