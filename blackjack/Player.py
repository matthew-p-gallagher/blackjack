
import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from blackjack.Hand import Hand


class Player:
    def __init__(self):
        self.hand = Hand()
        self.chips = 100
        self.stand = False

    def place_chips(self, chips):
        if chips > self.chips:
            print("Can't place + " + str(chips) + " chips")
            print("You only have " + str(self.chips) + " chips")
            return 0
        else:
            self.chips -= chips
            return chips

    def choose_bet(self):
        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print("Please enter an integer")
            self.choose_bet()
        return bet

    def place_insurance(self, cost):
        choice = input("Place insurance? (y/n): ")
        if choice == "y":
            return self.place_chips(cost)
        else:
            print("No insurance")
            return 0

    def add_chips(self, chips):
        self.chips += chips

    def reset(self):
        self.hand.reset()
        self.stand = False
