n = int(input("Введите количество коров "))
last_two = n % 100
if last_two % 10 == 1 and last_two != 11:
    print(last_two, " корова")
elif 2 <= last_two % 10 <= 4 or 12 <= last_two <= 14:
    print(last_two, " коровы")
else:
    print(n, " коров")
