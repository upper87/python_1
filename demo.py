# ===================
# Цикл вайл
# ===================

# n = int(input("n:"))
#
# count = 0
#
# while count < n:
#     print("Hello")
#     count += 1

# ===================
# Строки
# ===================

# first = int(input())
# end = int(input())
# step = int(input())

# name = "Василий"
#
# # print(name[first:end:step])
# # name = name.upper()
# result = name.count('ли')
# result_digital = name.isdigit()
# result_find = name.find("ий")
# print(result, result_digital, result_find)

# ===================
# Списки
# ===================

# my_list = []
#
# my_list.append(10)
# my_list.append("hello")
# my_list.append(2.55)
# my_list.append(10)
# my_list.insert(2, "World")
# my_list.pop(2)
# my_list.remove(10)
# my_list.reverse()
# my_list = my_list[::-1]
#
# my_list = tuple(my_list)
#
# print(my_list, type(my_list))
#
# i= 0
#
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#
# for list in my_list:
#     print(list)

numbers = [2, 4, 0, - 35, 20, -5, 0, -45]

num_positive = 0

for number in numbers:
    if number > 0:
        print(number)
