a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a>b:
    c1 = a
    a = b
    b = c1
if b>c:
    c1 = b
    b = c
    c = c1
if a>b:
    c1 = a
    a = b
    b = c1
print(a, b, c)