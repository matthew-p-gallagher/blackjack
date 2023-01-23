class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play_hand(self, bet):
        self.player.place_bet(bet)
