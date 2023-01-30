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

        self.img_path = f"images\\{suit}_{rank}.png"

    @staticmethod
    def validate_params(suit, rank) -> None:
        if suit not in range(4):
            raise ValueError("Invalid identifier int: suit")
        if rank not in range(1, 14):
            raise ValueError("Invalid identifier int: rank")

    def __eq__(self, other) -> bool:
        return self.suit == other.suit and self.rank == other.rank

    def __str__(self) -> str:

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        suit_str = suits[self.suit]

        if self.rank == 1:
            rank_str = "Ace"
        elif self.rank == 11:
            rank_str = "Jack"
        elif self.rank == 12:
            rank_str = "Queen"
        elif self.rank == 13:
            rank_str = "King"
        else:
            rank_str = str(self.rank)

        return f"{rank_str} of {suit_str}"
