def distance(x1, y1, x2, y2):
    dist = (((x2-x1)**2)+((y2-y1)**2)) ** 0.5
    return dist
def can_triangle(p1, p2, p3):
    # a = distance(p1[0], p1[1], p2[0], p2[1])
    a = distance(*p1, *p2)
    b = distance(*p2, *p3)
    c = distance(*p1, *p3)
    return a + b > c and a + c > b and b + c > a

res = can_triangle((10, 12), (14, 1118), (12, 12))
print(res)
