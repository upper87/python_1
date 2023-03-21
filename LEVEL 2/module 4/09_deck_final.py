import random
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
    def __gt__(self, other_card):
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

    def __lt__(self, other_card):
        return not self.__gt__(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))
    def __getitem__(self, index):
        return self.cards[index]

    def __str__(self): # magic-method
        all_cards = []
        for card in self.cards:
            all_cards.append(card.__str__())
        return f'cards [{len(all_cards)}] {", ".join(all_cards)}'

    def draw(self, x):
        hand_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_cards

    def shuffle(self):
        random.shuffle(self.cards)



deck = Deck()
# TODO-final: реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())
# use __str__
#
card1, card2 = deck.draw(2)
# # 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())
print(card2)
#
# # 3. Сравнение карт:
if card1 < card2:
    print(f"{card1} меньше {card2}")
#
# # 4. Итерация по колоде:
# for card in deck:
#     print(card)
#
# # 5. Просмотр карты в колоде по ее индексу:
print(deck[6])
