x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

n1 = x1+y1
n2 = x2+y2
if (n1+n2) % 2 == 0:
    print("одного цвета")

else:
    print("разных цветов")
#print(n1, n2)