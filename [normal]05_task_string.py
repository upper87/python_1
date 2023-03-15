text = "В теории, теория и практика неразделимы. На практике это не так."
vowels = "ауоыэяюёие"
i = 0
i_1 = 0
sym = 0
a = str(text[0])
b = str(text[0])

while i < len(low):
    a = text[i]
    # print(a)
    i += 1
    while i_1 < len(vowels):
        b = vowels[i_1]
        # print(b)
        if a == b:
            sym += 1
        i_1 += 1
    i_1 = 0
print(sym)
