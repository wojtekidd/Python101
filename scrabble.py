letters_table = ["a", "b", "c", "d",
                 "e", "f", "g", "h",
                 "i", "j", "k", "l",
                 "m", "n", "o", "p",
                 "r", "s", "t", "u",
                 "v", "w", "x", "y", "z"
                 ]
letters_val = {}.fromkeys(letters_table, 0)
letters_val["a"] = 5
letters_val["p"] = 3

word = input("Give me a word: ")

scrabble_sum = 0

for character in word:
    scrabble_sum += letters_val[character.lower()]

print(scrabble_sum)






