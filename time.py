hour = int(input("первое число "))
minutes = int(input("второе число "))

if hour<24 and minutes<60:
    print("Может")
else:
    print("Не может")