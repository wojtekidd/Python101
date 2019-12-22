from dashboard.abs_observer import AbsObserver


class Observer(AbsObserver):
    _open_tickets = 0
    _close_tickets = 0
    _assigned_tickets = 0

    def __init__(self, subject):
        self._subject = subject
        subject.attach(self)

    def detach(self, subject):
        subject.detach(self)
