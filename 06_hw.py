items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
#
# itemm = []
#
# for item in items:
#     itemm.append(item["brand"])
# no_dupes = [x for n, x in enumerate(itemm) if x not in itemm[:n]]
# # for num1, item in enumerate(items):
# #     for n, a in enumerate(item):
# #         if num1 == n:
# #             brands += (item['brand'])
# print(f"Товары на складе представлены брэндами: {no_dupes}")
#
# max_num = 0
# max_index = 0
# a = ""
# b = 0
#
#
#
#
# print(max_list)
# # for item in items:
# #     print("Товары на складе представлены брэндами: ")
# #
# #     # TODO: your code here
# #
# #     print("На складе больше всего товаров брэнда(ов): ")
# #
# #     # TODO: your code here
# #
# #     print("На складе самый дорогой товар брэнда(ов): ")
# #
# #     # TODO: your code here
#
# print("Товары на складе представлены брэндами: ")
brands = {}
max_brand_name = ""
max_brand_cnt = 0
max_cost_name = ""
max_cost = 0
for item in items:
    if item["brand"] in brands:
        brands[item["brand"]] += 1
    else:
        brands[item["brand"]] = 1
    if max_brand_cnt < brands[item["brand"]]:
        max_brand_cnt = brands[item["brand"]]
        max_brand_name = item["brand"]
    if max_cost < item["price"]:
        max_cost = item["price"]
        max_cost_name = item["brand"]


print(f"Товары на складе представлены брэндами: {list(brands.keys())}")
print("На складе больше всего товаров брэнда(ов): {}, {} шт".format(max_brand_name, max_brand_cnt))
print("На складе самый дорогой товар брэнда(ов): %s, %s" % (max_cost_name, max_cost))
