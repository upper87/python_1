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


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)

cards_str = []
for card in cards:
    cards_str.append(card.to_str())

result = ",".join(cards_str)
print(f"cards [{len(cards_str)}] {result}")
