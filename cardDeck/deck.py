from card import Card
from random import shuffle


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def _deal(self, num):
        count = self.count()
        deal_num = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-deal_num:]
        self.cards = self.cards[0:-deal_num]
        return hand

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

    def count(self):
        return len(self.cards)


deck = Deck()
print(deck.cards)
print(deck.count())
print(deck)
print(deck._deal(5))
deck.shuffle()
print(deck.cards)
print(deck.deal_card())
print(deck.deal_hand(5))
print(deck.cards)
print(deck.count())
