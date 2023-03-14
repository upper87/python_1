n = int(input("Введите количество коров "))

if (n%10) == 1:
    print(n, " корова")
elif (n%10) == 2 or (n%10) == 3 or (n%10) == 4:
    print(n, " коровы")
else :
    print(n, " коров")