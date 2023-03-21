import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        values_weigth = {
            '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
            '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13
        }
        suits_weigth = {
            "Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4
        }
        if values_weigth[self.value] > values_weigth[other_card.value]:
            return True
        elif values_weigth[self.value] < values_weigth[other_card.value]:
            return False
        else:
            return suits_weigth[self.suit] > suits_weigth[other_card.suit]

    def less(self, other_card):
        return not self.more(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        all_cards = []
        for card in self.cards:
            all_cards.append(card.to_str())
        return f'cards [{len(all_cards)}] {", ".join(all_cards)}'

    def draw(self, x):
        hand_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_cards

    def shuffle(self):
        random.shuffle(self.cards)

    ...


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
