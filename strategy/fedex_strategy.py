from strategy.abs_strategy import AbsStrategy


class FedexStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.0
