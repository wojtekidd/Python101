import abc


class AbsStrategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def calculate(self, value):
        pass
