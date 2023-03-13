number = int(input("Введите четырехзначное число: "))

n1 = number // 1000
n22 = number // 10
n33 = number % 1000
n2 = n33 // 100
n3 = n22 % 10
n4 = number % 10

print(n1)
print(n2)
print(n3)
print(n4)