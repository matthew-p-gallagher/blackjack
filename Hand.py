from Card import Card
from Deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.bust = False

    def add_card(self, card):
        self.cards.append(card)
        self.total += card.score
        if self.total > 21:
            self.bust = True


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
