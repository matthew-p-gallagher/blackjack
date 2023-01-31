import random


class Card:
    def __init__(self, suit: int, rank: int) -> None:
        self.validate_params(suit, rank)
        self.suit = suit
        self.rank = rank
        self.soft = False

        # Ace score
        if self.rank == 1:
            self.soft = True
            self.score = 11
        # Face cards score
        elif self.rank > 10:
            self.score = 10
        # Number cards score
        else:
            self.score = self.rank

        self.id = self.create_id()

    @staticmethod
    def validate_params(suit, rank) -> None:
        if suit not in range(4):
            raise ValueError("Invalid identifier int: suit")
        if rank not in range(1, 14):
            raise ValueError("Invalid identifier int: rank")

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def create_id(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        suit_str = suits[self.suit]

        if self.rank == 1:
            rank_str = "ace"
        elif self.rank == 11:
            rank_str = "jack"
        elif self.rank == 12:
            rank_str = "queen"
        elif self.rank == 13:
            rank_str = "king"
        else:
            rank_str = str(self.rank)

        return f"{rank_str}_of_{suit_str}"

    def __str__(self):
        return self.id


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def encode_deck(self):
        self.encoded = ""
        for card in self.cards:
            self.encoded += str(card.suit) + str(card.rank)

    def shuffle(self):
        random.shuffle(self.cards)
        self.encode_deck()

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

    def no_of_cards(self):
        return len(self.cards)

    def reset(self):
        self.__init__()


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
                # display_total()
                print(f"Player total: {self.total}" + " soft" * int(self.soft))
            else:
                self.bust = True
                # display_total()
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

    def place_insurance(self, cost, choice=None):
        if choice is None:
            choice = input("Place insurance? (y/n): ")
        if choice == "y":
            return self.place_chips(cost)
        elif choice == "n":
            print("No insurance")
            return 0
        else:
            print("Please enter y or n")
            self.place_insurance(cost)

    def add_chips(self, chips):
        self.chips += chips

    def reset(self):
        self.hand.reset()
        self.stand = False


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def reset(self):
        self.hand.reset()


class Game:
    def __init__(self):
        self.inplay = False
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.pot = 0

    def display_info(self):
        print(
            f"""
        ---Blackjack---

        Dealer stands on 17
        Insurance pays 2:1
        
        You have  {str(self.player.chips)} chips
        """
        )

    def play_round(self, bet):
        self.pot = bet
        self.deal_cards()
        # if not self.check_player_blackjack():
        #     if not self.check_dealer_blackjack():
        #         self.player_play()
        #         if self.player.hand.bust:
        #             print(self.dealer.hand.cards[1])
        #             print(f"Dealer total: {self.dealer.hand.total}")
        #             print("You lose")
        #             print("You have " + str(self.player.chips) + " chips")
        #         else:
        #             self.dealer_play()
        #         if not (self.player.hand.bust or self.dealer.hand.bust):
        #             if self.player.hand.total > self.dealer.hand.total:
        #                 print("You win!")
        #                 self.pot *= 2
        #             elif self.player.hand.total == self.dealer.hand.total:
        #                 print("Push")
        #             else:
        #                 print("You lose")
        # self.pay_out()
        # self.game_reset()

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

    def check_player_blackjack(self):
        if self.player.hand.total == 21:
            print(self.dealer.hand.cards[1])
            if self.dealer.hand.total == 21:
                print("Push")
            else:
                print("Blackjack!")
                self.pot *= 2.5
            return True
        else:
            return False

    def check_dealer_blackjack(self, choice=None):
        if self.dealer.hand.cards[0].rank == 1:
            cost = self.pot / 2
            print("Dealer has an Ace")
            print("Insurance costs " + str(cost) + " chips")
            insurance = self.player.place_insurance(cost, choice)
            if self.dealer.hand.total == 21:
                print("Dealer has Blackjack!")
                self.pot = insurance * 3
                return True
        return False

    def hit_or_stand(self, choice=None):
        if choice == None:
            choice = input("Hit or Stand? (h/s): ")

        if choice == "h":
            self.player.hand.add_card(self.deck.deal())
            print(self.player.hand.cards[-1])
            print(
                f"Player total: {self.player.hand.total}"
                + " soft" * int(self.player.hand.soft)
            )
            if not self.player.hand.bust:
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
        self.pot = 0

    def deal_cards(self):
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())

    def game_reset(self):
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()
        self.pot = 0


if __name__ == "__main__":
    game = Game()
    game.display_info()
    while True:
        game.play()
