d = {
    "a": 4,
    "b": 5,
    "c": 6,
    "d": 9
}
cum = 0

for item in d.values():
    if type(item) == int:
        print(item)
    cum += item

print(cum)
