from Deck import Deck
from Player import Player
from Dealer import Dealer


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.pot = 0

    def display_info(self):
        print("---Blackjack---")
        print()
        print("Dealer stands on 17")
        print("Insurance pays 3:2")
        print()
        print("You have " + str(self.player.chips) + " chips")
        print()

    def play(self):

        self.pot = self.player.place_bet()
        self.deal_cards()
        self.check_blackjack()
        self.hit_or_stand()

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
            cost = self.pot // 2
            print("Dealer has an Ace")
            print("Insurance costs " + str(cost) + " chips")
            insurance = self.player.place_insurance(cost)
            if self.dealer.hand.total == 21:
                print("Dealer has Blackjack!")
                self.pot = insurance * 3
                self.pay_out()

    def pay_out(self):
        print(f"You win {self.pot}")
        self.player.add_chips(self.pot)

    def deal_cards(self):
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        print("Player's hand: ")
        for card in self.player.hand.cards:
            print(card)
        print(f"Player total: {self.player.hand.total}")

        print("Dealer's hand: ")
        print(self.dealer.hand.cards[0])
        print("----------")

    def hit_or_stand(self):

        choice = input("Hit or Stand? (h/s): ")
        if choice == "h":
            self.player.hand.add_card(self.deck.deal())

            print(self.player.hand.cards[-1])
            print(f"Player total: {self.player.hand.total}")
            if self.player.hand.bust:
                print("You busted!")
            else:
                self.hit_or_stand()
        elif choice == "s":
            print("You stand on ", self.player.hand.total)
        else:
            print("Please enter h or s.")
            self.hit_or_stand()


if __name__ == "__main__":
    game = Game()
    game.display_info()
    game.play()
