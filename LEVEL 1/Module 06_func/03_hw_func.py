# (a1 - a2)^2 + (b1-b2)^2 < (r-r2)^2

def circle_in_circle(x1, y1, x2, y2, r1, r2):
    return ((x1 - x2) ** 2) + ((y1 - y2) ** 2) < (r1 - r2) ** 2


print(circle_in_circle(1, 0, 2, 0, 6, 1))
