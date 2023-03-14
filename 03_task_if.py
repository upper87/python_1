cash = int(input("Введите деньги: "))
cost = int(input("Введите цену товара: "))

if cash < cost:
    print("Денег не достаточно")
elif cash > cost:
    change = cost - cash
    print("Ваша сдача", abs(change))
else:
    print("Сдачи нет")