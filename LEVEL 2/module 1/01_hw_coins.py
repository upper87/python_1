import random
class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.randint(0, 1)
        if self.side == 0:
            return self.side = "Решка"
        else:
            return self.side = "Орел"

n_coins = int(input("Введите количество монеток: "))
i = 0


while i < n_coins:
    coin = Coin()
    coin.flip()
    print(coin.side)
    i += 1
# coins_list = []
# i = 0
#


# for coin in coins_list:
#     # print(coin.side)
#     print(coin_flip)

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())