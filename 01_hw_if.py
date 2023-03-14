n = int(input("n: "))
m = int(input("m: "))
k = int(input("k: "))

if k < m * n and (k % m == 0 or k % n == 0):
    print("Да")
else:
    print("Нет")
