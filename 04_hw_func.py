def pars_input_drob(drob_str):
    drob = drob_str
    index_integer = drob.find(" ")
    index_div = drob.find("/")
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
    list_drob = integer, chislitel, znamenatel
    return list_drob

# def nod_evklid(chislitel,znamenatel):
#     q1 = chislitel / znamenatel


print("Введите первую дробь в формате n x/y: ", end="")
drob = pars_input_drob(input())
integer = drob[0]
chislitel = drob[1]
znamenatel = drob[2]
print(integer, chislitel, znamenatel)
print("Введите вторую дробь в формате n x/y: ", end="")
drob2 = pars_input_drob(input())
integer2 = drob2[0]
chislitel2 = drob2[1]
znamenatel2 = drob2[2]
print(integer2, chislitel2, znamenatel2)

if integer == 0 and integer2 == 0:
    res_integer = 0
elif integer != 0 and integer2 != 0:
    res_integer = integer + integer2
elif integer == 0:
    res_integer = integer2
elif integer2 == 0:
    res_integer = integer2


print(res_integer)
#
# if znamenatel == znamenatel2 or znamenatel == 0 or znamenatel2 == 0:
#     res_chislitel = chislitel + chislitel2
#     res_znamenatel = znamenatel
# else:
#     general_znam = znamenatel * znamenatel2
#     chislitel = chislitel * znamenatel2
#     chislitel2 = chislitel2 * znamenatel
#     res_chislitel = chislitel + chislitel2
#     res_znamenatel = general_znam
#
# if res_chislitel > res_znamenatel:
#     while res_chislitel > res_znamenatel:
#         res_integer += 1
#         res_chislitel -= res_znamenatel
#
# if res_chislitel % 2 == 0 and res_znamenatel % 2 == 0 and res_chislitel != 0 and res_znamenatel != 0:
#     while True:
#         if res_chislitel % 2 == 0 or res_znamenatel % 2 == 0:
#             res_chislitel = res_chislitel // 2
#             res_znamenatel = res_znamenatel // 2
#         else:
#             break
#
# if res_chislitel % 2 == 1 or res_znamenatel % 2 == 1:
#     while res_znamenatel % 2 == 0 and res_chislitel == 1 or res_chislitel % 2 == 0 and res_znamenatel == 1:
#         res_chislitel = res_chislitel // 3
#         res_znamenatel = res_znamenatel // 3
#
# if res_chislitel > res_znamenatel:
#     while res_chislitel > res_znamenatel:
#         res_integer += 1
#         res_chislitel -= res_znamenatel
# if res_chislitel == res_znamenatel and res_chislitel != 0 and res_znamenatel != 0:
#     res_integer += 1
#     res_chislitel = 0
#     res_znamenatel = 0
#
# print(f"{res_integer} {res_chislitel}/{res_znamenatel} ")
#
#
