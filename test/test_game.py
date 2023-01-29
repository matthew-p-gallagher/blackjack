import pytest

from Game import Game
from Deck import Deck
from Player import Player
from Dealer import Dealer


@pytest.fixture
def game():
    return Game()


def test_game_init(game):
    assert game.pot == 0
    assert game.deck.no_of_cards() == 52
    assert game.player.chips == 100
