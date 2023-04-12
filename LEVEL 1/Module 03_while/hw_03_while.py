n = int(input("Введите число: "))
k = 0

line = ""
i = 0

while k < n:
    line = ""
    i = 0
    k += 1
    while i < n:
        i += 1
        line += str(i * k) + " "
    print(line)
