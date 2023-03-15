string = input("Введите пароль: ")
len = len(string)
spec = string.find("#")
upper = string.istitle()

if len > 8 and spec > 0 and upper == True:
    print("Подходит для пароля")
else:
    print("не подходит для пароля")

# print(len, spec, upper)