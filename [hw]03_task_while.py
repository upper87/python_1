n = int(input("n: "))
i = 1
i_1 = 1

print("таблица умножения для", n)

while i <= n:
    # if i <= n:
    while i_1 <= n:
        res = i*i_1
        print(res, end=" ")
        i_1 += 1
    print(end="\n")
    i_1 = 1
    i += 1