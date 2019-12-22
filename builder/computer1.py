class Computer:
    def __init__(self, case, mainboard, cpu, memory):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory

    def display(self):
        print(f"Custom configuration includes {self.case}, {self.mainboard}, {self.cpu}, {self.memory}")
