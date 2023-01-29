import pytest

from blackjack.Player import Player
from blackjack.Hand import Hand


@pytest.fixture
def player():
    return Player()


def test_player_init(player):
    assert player.hand.cards == []
    assert player.chips == 100
    assert player.stand == False


def test_place_chips_has_enough(player):
    assert player.chips == 100
    placed = player.place_chips(10)
    assert placed == 10
    assert player.chips == 90


def test_place_chips_remaining(player):
    player.place_chips(player.chips)
    assert player.chips == 0


def test_place_chips_not_enough(player):
    assert player.chips == 100
    placed = player.place_chips(110)
    assert placed == 0
    assert player.chips == 100


def test_add_chips(player):
    assert player.chips == 100
    player.add_chips(10)
    assert player.chips == 110
