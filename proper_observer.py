from dashboard.abs_observer import AbsObserver


class Observer(AbsObserver):
    _open_tickets = 0
    _closed_tickets = 0
    _assigned_tickets = 0

    def __init__(self, subject):
        self._subject = subject
        subject.attach(self)

    def detach(self, subject):
        subject.detach(self)

    def update(self):
        self._open_tickets = self._subject.open_tickets
        self._closed_tickets = self._subject.closed_tickets
        self._assigned_tickets = self._subject.assigned_tickets
        self.display()

    def display(self):
        print(f"Current open tickets:{self._open_tickets}")
        print(f"Current closed tickets:{self._closed_tickets}")
        print(f"Current assigned tickets:{self._assigned_tickets}\n")
