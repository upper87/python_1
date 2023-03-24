import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"

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
        values_weight = {
            '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
            '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13
        }
        suits_weight = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}
        if values_weight[self.value] > values_weight[other_card.value]:
            return True
        elif values_weight[self.value] < values_weight[other_card.value]:
            return False
        else:
            return suits_weight[self.suit] > suits_weight[other_card.suit]

    def __lt__(self, other_card):
        return not self > other_card


class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.__cards = []
        for suit in suits:
            for value in values:
                self.__cards.append(Card(value, suit))

    def __str__(self):  # magic-method
        all_cards = []
        for card in self.__cards:
            all_cards.append(str(card))
        return f'cards [{len(all_cards)}] {", ".join(all_cards)}'

    def draw(self, x):
        hand_cards = self.__cards[:x]
        self.__cards = self.__cards[x:]
        return hand_cards

    def shuffle(self):
        random.shuffle(self.__cards)

    def __getitem__(self, index):
        return self.__cards[index]