n = int(input("Количество карточек: "))
# Цикл, который выполнится n-1 раз
i = 1
sum_exist = 0
sum_all = 0

while i < n:
    card_number = int(input("Номер карточки: "))
    sum_exist += card_number
    i += 1
i = 1
while i <= n:
    sum_all = sum_all + i
    i += 1
card_number = sum_all - sum_exist
print("Номер потерянной карточки:", card_number)