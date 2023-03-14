n = int(input("n: "))
div = 2
is_prime = True

while div < n:
    if n % div == 0:
        print(div)
        is_prime = False
    div += 1
if is_prime:
    print("Число простое")