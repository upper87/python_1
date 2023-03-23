import random


class Dice:
    def __init__(self, num_sides=6):
        self.__num_sides = num_sides
        self.__side = None

    @property
    def side(self):  # геттер
        return self.__side

    @side.setter
    def side(self, new_value: int):  # сеттер
        if 1 <= new_value <= self.__num_sides and type(new_value) == int:
            self.__side = new_value
        else:
            raise ValueError(f"Только целое число [1, {self.__num_sides}]")

    def roll(self):
        self.__side = random.randint(1, self.__num_sides)

    def __gt__(self, other_dice: 'Dice'):
        if self.side is None or other_dice.side is None:
            raise TypeError("Нельзя сравнивать до подбрасывания")
        return self.side > other_dice.side

    def __lt__(self, other_dice: 'Dice'):
        if self.side is None or other_dice.side is None:
            raise TypeError("Нельзя сравнивать до подбрасывания")
        return self.side < other_dice.side

    def __eq__(self, other_dice: 'Dice'):
        if self.side is None or other_dice.side is None:
            raise TypeError("Нельзя сравнивать до подбрасывания")
        return self.side == other_dice.side


dice8 = Dice(8)
dice8.roll()
print(dice8.side)


def generate_dices(num: int) -> list:
    dices = []
    for i in range(num):
        dice_i = Dice()
        dices.append(dice_i)
    return dices



dices = generate_dices(10)
sides = []
for dice in dices:
    dice.roll()
    sides.append(dice.side)
# print(sides)

for i in range(1, 7):
    if sides.count(i) != 0:
        print(f"{i}-ка выпала у кубика {sides.count(i)}")