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

        return f"{self.value} {icons[self.suit]}"

    def equal_suite(self, other_card):
        return self.suit == other_card




values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []

for value in values:
    card = Card(value, "Hearts")
    hearts_cards.append(card)



hearts_cards_str = []
for card in hearts_cards:
    hearts_cards_str.append(card.to_str())

result = ",".join(hearts_cards_str)
print(result)


diamonds_cards = []

for value in values:
    card = Card(value, "Diamonds")
    diamonds_cards.append(card)


diamonds_cards_str = []
for card in diamonds_cards:
    diamonds_cards_str.append(card.to_str())

result1 = ",".join(diamonds_cards_str)
print(result1)

