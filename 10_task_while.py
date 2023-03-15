a = int(input("a: "))
b = int(input("b: "))

count = 0
while a < b:
    i = 1
    result = 0
    while i < a:
        if a % i == 0:
            result = result + i
        i += 1
    if result == a:
        count += 1
    a += 1
print("Общее количество совершенных чисел в диапазоне:", count, "Число:", result)