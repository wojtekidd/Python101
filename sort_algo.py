

def letter_index(x, string):
    for i in range(len(string)):
        if string[i] == x:
            return i


print(letter_index("a", "Ala ma kota."))
