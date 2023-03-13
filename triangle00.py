a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

p = a + b + c
p2 = p / 2
s = (p2*(p2-a)*(p2-b)*(p2-c))**0.5

print("p =", p)
print("s =", s)