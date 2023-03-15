# fruits = ["яблоко", "банан", "киви", "арбуз", "картошечка", "марковка"]
# long_index = 0
# long_index_start = 0
# num = 0
# leng_fr = 0
# final_fr = ""
# space = " "
# looong_str = ""
#
# for leng in fruits:
#     long_index = len(leng)
#     if long_index_start < long_index:
#         long_index_start = long_index
#         looong_str = leng
# print(long_index_start)
#
# for list in fruits:
#     num += 1
#     leng_fr = len(list)
#     if leng_fr < long_index_start:
#         final_fr = (space * (long_index_start - len(list)) ) + list
#     else:
#         final_fr = looong_str
#
#     print(num, final_fr)

fruits = ["яблоко", "банан", "киви", "арбуз", "картошечка", "марковка"]
space = " "
max_length = 0

for fruit in fruits:
    if len(fruit) > max_length:
        max_length = len(fruit)

for i, fruit in enumerate(fruits,1):
    print(str(i) + ".", fruit.rjust(max_length, space))
