def distance(x1, y1, x2, y2):
    dist = (((x2-x1)**2)+((y2-y1)**2)) ** 0.5
    return dist


# Тестируем функцию
print(distance(2, 4, 2, 9))
print(distance(12, 8, 12, -9))
print(distance(23, 0, 15, 32))