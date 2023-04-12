class Money:
    def __init__(self, rub, kopeyka):
        self.__kopek = rub * 100 + kopeyka

    def __str__(self):
        rub = abs(self.__kopek) // 100
        kop = abs(self.__kopek) % 100
        if self.__kopek < 0:
            return f"-{rub}руб {kop}коп"
        else:
            return f"{rub}руб {kop}коп"

    def __add__(self, other):
        return Money(0, self.__kopek + other.__kopek)

    def __sub__(self, other):
        return Money(0, self.__kopek - other.__kopek)

money1 = Money(10, 39)
money2 = Money(12, 49)
money3 = money1 - money2
print(money3)