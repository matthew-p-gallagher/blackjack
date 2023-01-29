from Card import Card
from Deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.soft = False
        self.bust = False

    def add_card(self, card):
        self.cards.append(card)
        if card.soft:
            self.soft = True
        self.total += card.score
        if self.total > 21:
            self.bust = True

    def remove_soft(self):
        for i in range(len(self.cards)):
            if self.cards[i].soft:
                self.cards[i].soft = False
                break

        for card in self.cards:
            if card.soft:
                return

        self.soft = False

    def reset(self):
        self.__init__()


if __name__ == "__main__":
    deck = Deck()
    hand = Hand()
    hand.add_card(deck.deal())
    hand.add_card(deck.deal())
    print(f"""
    {str(hand.cards[0])}
    {str(hand.cards[1])}
    Total:{hand.total}
    """)
