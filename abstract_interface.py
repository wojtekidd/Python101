import abc


class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self, value):
        pass

    @property
    @abc.abstractmethod
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    def __init__(self, value=None):
        self._my_prop = value

    def do_something(self, value):
        self._my_prop *= 2 + value

    @property
    def some_property(self):
        return self._my_prop


class BadClass(MyABC):
    pass


my_class = MyClass()
print(my_class)
bad_class = BadClass()