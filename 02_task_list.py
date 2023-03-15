# fruits = ["яблоко", "банан", "киви", "ананас", "груша"]
# num = 0
# for fruit in fruits:
#     num += 1
#     print(num, fruit)

fruits = ["яблоко", "банан", "киви", "ананас", "груша"]

for num, fruit in enumerate(fruits, 1):
    print(num, fruit)