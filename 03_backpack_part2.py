class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        # Возвращает строковое представление объекта Item
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = 30

    def add_item(self, item: Item) -> None:

        sum_weight = self.max_weight - self.sum_weight()
        if item.weight <= sum_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")


    def show_items(self) -> None:
        for item in self.items:
            print(item.show())
    # def max_weight(self, max_weight: int) -> int:
    #     self.__max_weight = max_weight



    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак

    def sum_weight(self) -> float:
        total_weigh = 0
        for item in self.items:
            total_weight += item.weight

        return total_weigh


    # def sum_cost(self) -> int:
    #     """
    #     Возвращает суммарную стоимость всех предметов в рюкзаке
    #     """
    #     # TODO: реализуйте метод


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)


# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack()

# Пытаемся добавлять предметы в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
# TODO: Если предмет не помещается в рюкзак по весу - вывести сообщение "Предмет {name} слишком тяжелый",
#  и сам предмет не должен быть добавлен в рюкзак.
#  Если предмет помещает, то добавляем его в рюкзак.

# Выводим все предметы в рюкзаке

backpack.show_items()