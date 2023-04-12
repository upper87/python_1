n = int(input("n: "))
i = 0
num_positive = 0  # Счетчик положительных чисел
while i < n:
    number = int(input("number: "))
    if number > 0:
        num_positive += 1
    i += 1
print("Было введено", num_positive, "положительных чисел")