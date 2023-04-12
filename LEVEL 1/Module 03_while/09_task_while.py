n = int(input("n: "))
div = 1
is_prime = True
perfect = 0

while div < n:
    if n % div == 0:
        perfect += div
        is_prime = False
    div += 1
if n == perfect:
    print("Число совершенное")
else:
    print("Число не совершенное")
if is_prime:
    print("Число простое")