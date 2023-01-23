class Player:
    def __init__(self):
        self.hand = Hand()
        self.chips = 100
        self.bet = 0

    def place_bet(self, bet):

        self.chips -= bet
        self.bet = bet
        self.hand.hit()
