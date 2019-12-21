import abc


class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def so_something(self, value):
        pass

