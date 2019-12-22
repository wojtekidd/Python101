from builder.computer4 import Computer

class MyComputer:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        self.get_case()
        self.build_mainboard()
        self.install_mainboard()

    def get_case(self):
       self._computer.case = "Coolmaster"

    def build_mainboard(self):
        self._computer.mainboard = "MSI"
        self._computer.cpu = "Intel"
        self._computer.memory = "16GB"

    def install_mainboard(self):
        pass

