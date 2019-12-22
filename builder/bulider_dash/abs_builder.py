import abc


class ABCBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def new_computer(self):
        pass

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def get_computer(self):
        pass