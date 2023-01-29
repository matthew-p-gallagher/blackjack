from Card import Card


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
            if self.soft:
                self.total -= 10
                self.remove_soft()
                print(f"Player total: {self.total}" +
                      " soft" * int(self.soft))
            else:
                self.bust = True
                print("You busted!")

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
    hand = Hand()
    card1 = Card(0, 1)
    card2 = Card(1, 1)
    hand.add_card(card1)
    hand.add_card(card2)
    print(hand.cards)
    print(hand.total)
    print(hand.soft)
    print(hand.bust)
