from abs_builder import ABCBuilder
from builder.computer4 import Computer

class ConcreteBuilder(ABCBuilder):

    def new_computer(self):
        self._computer = Computer()

    def get_case(self):
        self._computer.case = "Coolmaster"

    def build_mainboard(self):
        self._computer.mainboard = "MSI"
        self._computer.cpu = "Intel"
        self._computer.memory = "16 GB"

    def install_mainboard(self):
        return self._builder.get_computer()