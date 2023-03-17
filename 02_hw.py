import random

n = int(input("n: "))
# i = 0
numbers = []

# while i < n:
#     numbers.append(random.randint(-100, 100))
#     i += 1

for _ in range(n):
    numbers.append(random.randint(-100, 100))

print(numbers)
