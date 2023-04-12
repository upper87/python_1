name = input("1 строка: ")
surname = input("2 строка: ")

res1 = len(name)
res2 = len(surname)
if res2 > res1:
    print(surname)
elif res1 > res2:
    print(name)
else:
    print("Строки равны")