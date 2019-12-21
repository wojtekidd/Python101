from strategy.abs_strategy import AbsStrategy


class UPSStrategy(AbsStrategy):
    def calculate(self, order):
        return 4.0
