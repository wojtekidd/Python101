class Box:

    def __init__(self, something=[]):
        self.inside = something

    def put(self, something):
        self.inside.append(something)

    def retrieve(self):
        try:
            return self.inside.pop()
        except IndexError:
            return "The box is empty!"


box1 = Box()
box1.put("Dog")
box1.put("Cat")
box1.put("Chicken")

print(box1.retrieve())
print(box1.retrieve())
print(box1.retrieve())
print(box1.retrieve())
