from builder.computer3 import Computer

class MyComputer:

    def get_computer(self):
        return self._computer

    def build_computer(self):
        computer = self._computer = Computer()
        computer.case = "Coolermaster"
        computer.mainboard = "MSI 790"
        computer.cpu = "Intel core i7"
        computer.memory = "16 GB"

