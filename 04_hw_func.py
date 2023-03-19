drob = input("Введите 1 дробь в формате n x/y:")
drob2 = input("Введите 2 дробь в формате n x/y:")
index_integer = drob.find(" ")
index_div = drob.find("/")
index_integer2 = drob2.find(" ")
index_div2 = drob2.find("/")

if index_div == -1 and index_integer == -1:
    integer = int(drob)
    chislitel = 0
    znamenatel = 0
elif index_integer == -1:
    integer = 0
    chislitel = int(drob[0:index_div])
    znamenatel = int(drob[(index_div + 1):])
elif index_div == -1:
    integer = int(drob[0:index_integer])
    chislitel = 0
    znamenatel = 0
elif index_div >= 0 and index_integer >= 0:
    integer = int(drob[0:index_integer])
    chislitel = int(drob[(index_integer + 1):index_div])
    znamenatel = int(drob[(index_div + 1):])

print(integer, chislitel, znamenatel)

if index_div2 == -1 and index_integer2 == -1:
    integer2 = int(drob2)
    chislitel2 = 0
    znamenatel2 = 0
elif index_integer2 == -1:
    integer2 = 0
    chislitel2 = int(drob2[0:index_div2])
    znamenatel2 = int(drob2[(index_div2 + 1):])
elif index_div2 == -1:
    integer2 = int(drob2[0:index_integer2])
    chislitel2 = 0
    znamenatel2 = 0
elif index_div2 >= 0 and index_integer2 >= 0:
    integer2 = int(drob2[0:index_integer2])
    chislitel2 = int(drob2[(index_integer2 + 1):index_div2])
    znamenatel2 = int(drob2[(index_div2 + 1):])

print(integer2, chislitel2, znamenatel2)

# res_chislitel = "Отсутствует"
# res_znamenatel = "Отсутствует"

if integer == 0 and integer2 == 0:
    res_integer = 0
elif integer != 0 and integer2 != 0:
    res_integer = integer + integer2
elif integer == 0:
    res_integer = integer2
elif integer2 == 0:
    res_integer = integer2

if znamenatel == znamenatel2 or znamenatel == 0 or znamenatel2 == 0:
    res_chislitel = chislitel + chislitel2
    res_znamenatel = znamenatel
else:
    general_znam = znamenatel * znamenatel2
    chislitel = chislitel * znamenatel2
    chislitel2 = chislitel2 * znamenatel
    res_chislitel = chislitel + chislitel2
    res_znamenatel = general_znam

if res_chislitel % 2 == 0 and res_znamenatel % 2 == 0 and res_chislitel != 0 and res_znamenatel != 0:
    while res_chislitel % 2 == 0 or res_znamenatel % 2 == 0:
        res_chislitel = res_chislitel // 2
        res_znamenatel = res_znamenatel // 2

if res_chislitel % 2 == 1 or res_znamenatel % 2 == 1:
    while res_chislitel % 2 == 0 or res_znamenatel % 2 == 0:
        res_chislitel = res_chislitel // 3
        res_znamenatel = res_znamenatel // 3

if res_chislitel > res_znamenatel:
    while res_chislitel > res_znamenatel:
        res_integer += 1
        res_chislitel -= res_znamenatel
if res_chislitel == res_znamenatel and res_chislitel != 0 and res_znamenatel != 0:
    res_integer += 1
    res_chislitel = 0
    res_znamenatel = 0

print(f"{res_integer} {res_chislitel}/{res_znamenatel} ")


