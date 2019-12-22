from dashboard.abs_subject import AbsSubject


class Indicator(AbsSubject):
    _open_ticket = 0
    _closed_ticket = 0
    _assigned_ticket = 0

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self.closed_tickets

    @property
    def assigned_tickets(self):
        return self._assigned_tickets

    def set_indicators(self, open_tickets, closed_tickets, assigned_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._assigned_tickets = assigned_tickets
        self.notify()
