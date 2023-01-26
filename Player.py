from Hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()
        self.chips = 100

    def place_bet(self, bet):

        if bet > self.chips:
            print("You don't have enough chips to place that bet.")
        else:
            self.chips -= bet

    def add_chips(self, chips):
        self.chips += chips
