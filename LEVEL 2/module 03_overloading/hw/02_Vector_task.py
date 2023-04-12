class Vektr():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __add__(self, other_vektor):
        self.x = self.x + other_vektor.x
        self.y = self.y + other_vektor.y
        return f"Сумма {self.x} {self.y}"
    def __sub__(self, other_vektor):
        self.x = self.x - other_vektor.x
        self.y = self.y - other_vektor.y
        return f"Разность {self.x} {self.y}"

    def scalar(self, num: int):
        self.x *= num
        self.y *= num
        return f"Результат умножение на скаляр {num} : x={self.x} y={self.y}"

vek1 = Vektr(2,3)
vek2 = Vektr(4,5)
print(vek1 + vek2)
print(vek1 - vek2)
print(vek1.scalar(-3))