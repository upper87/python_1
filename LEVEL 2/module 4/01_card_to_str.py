# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": "\u2663",
            "Spades": "\u2660",
            "Clubs":"\u2666"
        }
        # if self.suit == "Hearts":
        #     suit = '\u2665'
        # elif self.suit == "Diamonds":
        #     suit = "\u2663"
        # elif self.suit == "Spades":
        #     suit = "\u2660"
        # elif self.suit == "Clubs":
        #     suit = "\u2666"
        return f"{self.value} {icons[self.suit]}"


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')