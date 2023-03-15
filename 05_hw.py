names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
leng = 0
final = ""

for name in names:
    if leng < len(name):
        leng = len(name)
        final = name

print(final)
