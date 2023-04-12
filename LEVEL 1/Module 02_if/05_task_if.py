number = int(input("Введите целое число число: "))

if number % 3 == 0 and not number % 5 == 0:
    print("Foo")
elif number % 5 == 0 and not number % 3 == 0:
    print("Bar")
elif (number % 3 == 0) and (number % 5 == 0):
    print("FooBar")
else:
    print(" ")