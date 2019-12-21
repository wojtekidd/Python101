from strategy.abs_strategy import AbsStrategy


class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.0
