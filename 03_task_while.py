n = int(input("n:"))
count = 0
sum = 0

while n >= count:
    if count % 2 == 0:
        sum += count
    count += 1

print(sum)
