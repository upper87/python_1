cost = float(input("Цена товара: "))
quantity = int(input("Количество товара: "))
i=1
sum = 0

while i <= quantity:
    sum += cost
    print(i, round(sum, 2), "рублей")
    i += 1