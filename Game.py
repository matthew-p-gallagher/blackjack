from Deck import Deck
from Player import Player
from Dealer import Dealer


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.bet = 0

    def play(self):
        self.deal_cards()
        print()
        self.hit_or_stand()

    def get_bet_amount(self):
        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print("Please enter a number.")
            self.get_bet_amount()
        return bet

    def deal_cards(self):
        self.player.place_bet(self.get_bet_amount())
        print("Player\t\t\tDealer")
        self.player.hand.add_card(self.deck.deal())
        print(self.player.hand.cards[0], end="\t\t")
        self.dealer.hand.add_card(self.deck.deal())
        print(self.dealer.hand.cards[0])
        self.player.hand.add_card(self.deck.deal())
        print(self.player.hand.cards[1], end="\t\t")
        self.dealer.hand.add_card(self.deck.deal())
        print("_______________")

    def hit_or_stand(self):
        print(f"Player total: {self.player.hand.total}")

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
    game.play()
