
drob = input("Введите 1 дробь в формате n x/y:")
drob2 = input("Введите 2 дробь в формате n x/y:")
index_integer = drob.find(" ")
index_div = drob.find("/")
index_integer2 = drob2.find(" ")
index_div2 = drob2.find("/")

if index_div == -1 and index_integer == -1:
    integer = int(drob)
    chislitel = "Числиитель отсутствует"
    znamenatel = "Знаменатель часть отсутствует"
elif index_integer == -1:
    integer = "Целая часть отсутствует"
    chislitel = int(drob[0:index_div])
    znamenatel = int(drob[(index_div+1):])
elif index_div == -1:
    integer = int(drob[0:index_integer])
    chislitel = "Числиитель отсутствует"
    znamenatel = "Знаменатель часть отсутствует"
elif index_div >= 0 and index_integer >= 0:
    integer = int(drob[0:index_integer])
    chislitel = int(drob[(index_integer+1):index_div])
    znamenatel = int(drob[(index_div+1):])


print(integer, chislitel, znamenatel)

if index_div2 == -1 and index_integer2 == -1:
    integer2 = int(drob2)
    chislitel2 = "Числиитель отсутствует"
    znamenatel2 = "Знаменатель часть отсутствует"
elif index_integer2 == -1:
    integer2 = "Целая часть отсутствует"
    chislitel2 = int(drob2[0:index_div2])
    znamenatel2 = int(drob2[(index_div2+1):])
elif index_div2 == -1:
    integer2 = int(drob2[0:index_integer2])
    chislitel2 = "Числиитель отсутствует"
    znamenatel2 = "Знаменатель часть отсутствует"
elif index_div2 >= 0 and index_integer2 >= 0:
    integer2 = int(drob2[0:index_integer2])
    chislitel2 = int(drob2[(index_integer2+1):index_div2])
    znamenatel2 = int(drob2[(index_div2+1):])

print(integer2, chislitel2, znamenatel2)

# res_chislitel = "Отсутствует"
# res_znamenatel = "Отсутствует"

if type(integer) == str and type(integer2) == str:
    res_integer = "Целая часть отсутствует"
elif type(integer) != str and type(integer2) != str:
    res_integer = integer + integer2
elif type(integer) == str:
    res_integer = integer2
elif type(integer2) == str:
    res_integer = integer2

if znamenatel == znamenatel2:
    res_chislitel = chislitel + chislitel2
    res_znamenatel = znamenatel
print(f"{res_integer} {res_chislitel}/{res_znamenatel} ")