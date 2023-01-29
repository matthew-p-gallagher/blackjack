import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from blackjack.Deck import Deck
from blackjack.Player import Player
from blackjack.Dealer import Dealer


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.pot = 0

    def display_info(self):
        print(f"""
        ---Blackjack---

        Dealer stands on 17
        Insurance pays 2:1
        
        You have  {str(self.player.chips)} chips
        """)

    def play(self):

        self.pot = self.player.choose_bet()
        self.deal_cards()
        self.check_player_blackjack()
        self.check_dealer_blackjack()
        self.player_play()
        if self.player.hand.bust:
            print(self.dealer.hand.cards[1])
            print(f"Dealer total: {self.dealer.hand.total}")
            print("You lose")
            print("You have " + str(self.player.chips) + " chips")
        else:
            self.dealer_play()
        if not (self.player.hand.bust or self.dealer.hand.bust):
            if self.player.hand.total > self.dealer.hand.total:
                print("You win!")
                self.pot *= 2
                self.pay_out()
            elif self.player.hand.total == self.dealer.hand.total:
                print("Push")
                self.pay_out()
            else:
                print("You lose")
        self.game_reset()

    def player_play(self):
        while not (self.player.stand or self.player.hand.bust):
            self.hit_or_stand()

    def dealer_play(self):
        print(self.dealer.hand.cards[1])
        while not (self.dealer.hand.total >= 17):
            self.dealer.hand.add_card(self.deck.deal())
            print(self.dealer.hand.cards[-1])

        print(f"Dealer total: {self.dealer.hand.total}")

        if self.dealer.hand.bust:
            print("Dealer busts!")
            self.pot *= 2
            self.pay_out()

    def check_player_blackjack(self):
        if self.player.hand.total == 21:
            print(self.dealer.hand.cards[1])
            if self.dealer.hand.total == 21:
                print("Push")
            else:
                print("Blackjack!")
                self.pot *= 2.5

    def check_dealer_blackjack(self):
        if self.dealer.hand.cards[0].rank == 1:
            cost = self.pot / 2
            print("Dealer has an Ace")
            print("Insurance costs " + str(cost) + " chips")
            insurance = self.player.place_insurance(cost)
            if self.dealer.hand.total == 21:
                print("Dealer has Blackjack!")
                self.pot = insurance * 3
                self.pay_out()

    def hit_or_stand(self, choice=None):
        if choice == None:
            choice = input("Hit or Stand? (h/s): ")

        if choice == "h":
            self.player.hand.add_card(self.deck.deal())
            print(self.player.hand.cards[-1])
            print(f"Player total: {self.player.hand.total}" +
                  " soft" * int(self.player.hand.soft))
            if self.player.hand.total == 21:
                self.player.stand = True
            else:
                self.hit_or_stand()
        elif choice == "s":
            print("You stand on ", self.player.hand.total)
            self.player.stand = True
        else:
            print("Please enter h or s.")
            self.hit_or_stand()

    def pay_out(self):
        print(f"You win {self.pot}")
        self.player.add_chips(self.pot)
        print("You have " + str(self.player.chips) + " chips")

    def deal_cards(self):
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        print("Player's hand: ")
        for card in self.player.hand.cards:
            print(card)
        print(f"Player total: {self.player.hand.total}" +
              " soft" * int(self.player.hand.soft))

        print("Dealer's hand: ")
        print(self.dealer.hand.cards[0])
        print("----------")

    def game_reset(self):
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()
