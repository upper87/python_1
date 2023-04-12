check = False

while check != True:
    x = int(input("Введите x слона "))
    y = int(input("Введите y слона "))
    x_enemy = int(input("Введите x врага "))
    y_enemy = int(input("Введите y врага "))
    if (x < 1 or x > 8) and (y < 1 or y > 8) and (x_enemy < 1 or x_enemy > 8) and (y_enemy < 1 or y_enemy > 8):
        print("Координата за шахматной доской")
    else:
        check = True
dif_x = x - x_enemy
dif_y = y - y_enemy
if abs(dif_x) == abs(dif_y):
    print("Слон бьет врага!")
else:
    print("Враг неуязвим!")