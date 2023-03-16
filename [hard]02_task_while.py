import math

# n = int(input("Введите сторону квадрата: "))
# symbo = input("Введите символ для отрисовки: ")
n = 4
symbo = "#"
space = " "
i = 0
i_1 = 0
prin1 = symbo
prin2 = symbo
dia = math.ceil(2 ** 0.5 * n)
print(dia)
dia2 = dia / 2

while i <= dia:
    while i_1 <= i:
        print(symbo, end="")
        i_1 += 1
    print(end="\n")
    print(space, end="")
    i_1 = 1
    i += 1


