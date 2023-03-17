text = input("Введите строку: ")
consonants = "бвгджзйклмнпрстфхцчшщ"
num_consonants = 0

for glob in text.lower():
    for word in consonants:
        if glob == word:
            num_consonants += 1

print("Согласных букв:", num_consonants)
