class Record():

    def __init__(self, title, year, artist):
        self.title = title
        self.year = year
        self.artist = artist

    def pretty(self):
        return f"{self.title} ({self.year}) by {self.artist}"


r1 = Record("Evil Empire", 1996, "Rage Against the Machine")
r2 = Record("Rage Against the Machine", 1992 , "Rage Against the Machine")

print(r1.pretty())
print(r2.pretty())

print(r1)

