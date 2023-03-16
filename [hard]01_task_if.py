check = False

while check != True:
    n = int(input("Введите четырехзначное число: "))
    if n < 1000 or n > 9999:
        print("Число не четырехзначное!")
    else:
        check = True


a = int(n/1000)
b = int((n - a*1000)/100)
c = int((n - (a*1000+b*100))/10)
d = n - (a*1000+b*100+c*10)
if a == d and b == c:
    print("Числа симметричны")
else:
    print("Числа не симметричны")
print(a, b, c, d)

