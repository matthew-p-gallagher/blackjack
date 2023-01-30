import pytest

from blackjack.Game import Game
from blackjack.Dealer import Dealer
from blackjack.Player import Player
from blackjack.Deck import Deck


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
    assert game.deck.no_of_cards() == 48
