import abc
from dashboard.abs_observer import AbsObserver


class AbsSubject(metaclass=abc.ABCMeta):
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("Observer not derived from AbsObserver")
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self):
        for observer in self._observers:
            observer.update()
