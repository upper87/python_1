import random

n = random.randint(1, 15)
i = 0
numbers = []
final_numbers = []
sq = 0

while i < n:
    numbers.append(random.randint(0, 100))
    i += 1

print("Сгенерированный список:", numbers)

for number in numbers:
    sq = number**0.5
    if sq % 1 == 0:
        final_numbers.append(number)

print("Список чисел имеющие квадратные корни:", final_numbers)