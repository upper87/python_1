levels = int(input("levels: "))
i = 1
s = 0
sym = 0

while i <= levels:
    s = i * i
    i += 1
    sym = sym + s

print(sym)
