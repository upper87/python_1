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

# numbers = [2, 4, 0, - 35, 20, -5, 0, -45]
#
# num_positive = 0
#
# for number in numbers:
#     if number > 0:
#         print(number)

# people = {
#     "name" : "Иван",
#     "age" : 34,
#     "address" : {
#         "city" : "Москва",
#         "street" : "ploshad"
#     }
# }
# print(people["address"]["street"])
# print(people["age"])

# item = {
#     "title": "Кепка",
#     "color": "Черный",
#     "cost": "1300"
# }
# item["cost"] = 1500
# item["brand"] = "rebook"
# del item["color"]
# item["colors"] = ["black", "red", "white"]
# print(item)

# items = [
#     {
#      "title": "Кепка",
#      "color": "Черный",
#      "cost": "1300"
#     },
#     {
#         "title": "Кимано",
#         "color": "Белый",
#         "cost": "300"
#     },
#     {
#         "title": "Штаны",
#         "color": "Зеленые",
#         "cost": "2500"
#     }
#
# ]
# print(items[1]["title"])
# for num, item in enumerate(items,1):
#     print(f"{num}. {item['title']}")


# def sum2(a, b):
#     c = a + b
#     return c
#
# res = sum2(2, 3)
# print(res)

# def my_max(*args):
#     max_value = args[0]
#     for arg in args:
#         if arg > max_value:
#             max_value = arg
#     return max_value
#     print(args)
#
# res = my_max(3)
# res = my_max(3,6)
# # res = my_max(1,2,3,4,5)
# print(res)

# import lib
# from lib import distance
# import sys
# import requests
# resault = requests.get("https://oldteam.us")
# print(resault.content)
#
# print(sys.path)
#
# print(lib.palindrome(12321))
#
# print(distance(1, 2, 3, 4))

# Class's

# class Item:
#     def __init__(self, name, color, cost):
#         self.name = name
#         self.color = color
#         self.cost = cost
#
#
# item1 = Item("кепка", "синний", 1400)
# item2 = Item("Кеды", "красные", 1000)
# item3 = Item("футбоолка", "Бедая", 500)
#
# print(item2.name)
#
# my_list = [2, 3, 4, 5]
# print(my_list)
# def square(n):
#     return n * n


# numbers = [2, 5, 6, 7]
#
# sum(numbers)
# # res = list(map(square, numbers))
#
# res = sum(list(map(lambda n: n*n, numbers)))
# print(res)

class Item:
    def __init__(self, name, cost):
        self.name = name1
        self.cost = cost

item1 = Item("Банка", 100)
item2 = Item("Палка", 200)