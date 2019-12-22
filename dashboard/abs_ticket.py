import abc


class AbsTicket(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def display(self, number):
        pass

    @abc.abstractmethod
    @property
    def property(self, ongoing=boolean, ):