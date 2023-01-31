import pytest

from logic.Game import Game
from logic.Dealer import Dealer
from logic.Player import Player
from logic.Deck import Deck
from logic.Card import Card


@pytest.fixture
def game():
    return Game()


def test_game_init(game):
    assert game.pot == 0
    assert game.deck.no_of_cards() == 52
    assert game.player.chips == 100


def test_deal_cards(game):
    game.deal_cards()
    assert len(game.player.hand.cards) == 2
    assert len(game.dealer.hand.cards) == 2
    assert (
        game.player.hand.cards[0] != game.player.hand.cards[1]
        and game.player.hand.cards[0] != game.dealer.hand.cards[0]
        and game.player.hand.cards[0] != game.dealer.hand.cards[1]
        and game.player.hand.cards[1] != game.dealer.hand.cards[0]
        and game.player.hand.cards[1] != game.dealer.hand.cards[1]
        and game.dealer.hand.cards[0] != game.dealer.hand.cards[1]
    )
    assert game.deck.no_of_cards() == 48


def check_player_blackjack(game):

    # Player has blackjack, dealer doesn't
    game.pot = 100
    game.player.hand.cards = [Card(1, 1), Card(2, 12)]
    game.dealer.hand.cards = [Card(1, 5), Card(2, 6)]
    assert game.check_player_blackjack() == True
    assert game.pot == 250

    # Player has blackjack, dealer has blackjack
    game.pot = 100
    game.player.hand.cards = [Card(1, 1), Card(2, 12)]
    game.dealer.hand.cards = [Card(1, 1), Card(2, 12)]
    assert game.check_player_blackjack() == True
    assert game.pot == 100

    # Player doesn't have blackjack
    game.pot = 100
    game.player.hand.cards = [Card(1, 1), Card(2, 11)]
    game.dealer.hand.cards = [Card(1, 1), Card(2, 12)]
    assert game.check_player_blackjack() == False
    assert game.pot == 100


def test_dealer_blackjack(game):

    # Dealer first card ace, takes insurance, has blackjack
    game.pot = 100
    game.player.chips = 100
    game.dealer.hand.add_card(Card(1, 1))
    game.dealer.hand.add_card(Card(2, 13))
    assert game.check_dealer_blackjack(choice="y") == True
    assert game.pot == 150
    assert game.player.chips == 50
    game.game_reset()

    # Dealer first card ace, doesn't take insurance, has blackjack
    game.pot = 100
    game.player.chips = 100
    game.dealer.hand.add_card(Card(1, 1))
    game.dealer.hand.add_card(Card(2, 13))
    assert game.check_dealer_blackjack(choice="n") == True
    assert game.pot == 0
    assert game.player.chips == 100
    game.game_reset()

    # Dealer first card ace, takes insurance, no blackjack
    game.pot = 100
    game.player.chips = 100
    game.dealer.hand.add_card(Card(1, 1))
    game.dealer.hand.add_card(Card(2, 7))
    assert game.check_dealer_blackjack(choice="y") == False
    assert game.pot == 100
    assert game.player.chips == 50
    game.game_reset()

    # Dealer first card ace, doesn't take insurance, no blackjack
    game.pot = 100
    game.player.chips = 100
    game.dealer.hand.add_card(Card(1, 1))
    game.dealer.hand.add_card(Card(2, 7))
    assert game.check_dealer_blackjack(choice="n") == False
    assert game.pot == 100
    assert game.player.chips == 100
    game.game_reset()

    # Dealer first card not ace
    game.pot = 100
    game.player.chips = 100
    game.dealer.hand.add_card(Card(3, 3))
    game.dealer.hand.add_card(Card(1, 1))
    assert game.check_dealer_blackjack(choice="n") == False
    game.game_reset()


def test_pay_out(game):
    game.player.chips = 100
    game.pot = 50
    game.pay_out()
    assert game.player.chips == 150
    assert game.pot == 0


def test_game_reset(game):
    game.player.chips = 50
    game.pot = 50
    game.deal_cards()
    game.game_reset()
    assert game.player.chips == 50
    assert game.pot == 0
    assert game.deck.no_of_cards() == 52
    assert len(game.player.hand.cards) == 0
    assert len(game.dealer.hand.cards) == 0
