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
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)
    # def add_cards(self):




    def show(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f"{join(cards_str)}"


# Создаем колоду
deck = Deck()


# Выводим колоду в формате указанном в основном задании
print(deck.show())
