import random

n = int(input("n: "))
i = 0
numbers = []
sym = 0

while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1

for word in numbers:
    if word > 0 and word % 2 == 0:
        sym += word

print(numbers)
print(sym)
