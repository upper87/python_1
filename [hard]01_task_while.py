n = int(input("n: "))
i = 1
i_1 = 1
sum = 0
second_feb = 1

while i <= n:
    sum = sum + second_feb
    second_feb = sum - second_feb
    i += 1
    print(sum, end=" ")
