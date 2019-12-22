import abc


class ABCBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def build_part(self):
        pass
