class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

my_counter = Counter(4,10)
print(iter(my_counter))
print(my_counter.current)
for item in my_counter:
    print(item)