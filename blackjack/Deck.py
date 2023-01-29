from blackjack.Card import Card
import random

import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def encode_deck(self):
        self.encoded = ""
        for card in self.cards:
            self.encoded += str(card.suit) + str(card.rank)

    def shuffle(self):
        random.shuffle(self.cards)
        self.encode_deck()

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
