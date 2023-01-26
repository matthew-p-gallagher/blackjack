import random

from Card import Card


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

    def no_of_cards(self):
        return len(self.cards)

    def reset(self):
        self.__init__()


if __name__ == "__main__":
    deck = Deck()
    card1 = deck.deal()

    print(str(card1))
    print(deck.no_of_cards())

    deck.reset()

    print(deck.no_of_cards())
