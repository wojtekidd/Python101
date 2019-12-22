from builder.bulider_dash.director import Director
from builder.bulider_dash.concrete_builder import ConcreteBuilder

computer_builder = Director(ConcreteBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()
