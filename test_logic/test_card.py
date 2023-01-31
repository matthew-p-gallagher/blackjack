import pytest

from game_logic import Card


def test_card_init():
    # Ace
    card = Card(0, 1)
    assert card.suit == 0
    assert card.rank == 1
    assert card.soft
    assert card.score == 11
    assert card.id == "ace_of_hearts"

    # Jack
    card = Card(1, 11)
    assert card.suit == 1
    assert card.rank == 11
    assert not card.soft
    assert card.score == 10
    assert card.id == "jack_of_diamonds"

    # King
    card = Card(2, 13)
    assert card.suit == 2
    assert card.rank == 13
    assert not card.soft
    assert card.score == 10
    assert card.id == "king_of_clubs"

    # Number card
    card = Card(3, 5)
    assert card.suit == 3
    assert card.rank == 5
    assert not card.soft
    assert card.score == 5
    assert card.id == "5_of_spades"


def test_card_validate_params():
    # Invalid suit
    with pytest.raises(ValueError):
        Card.validate_params(-1, 1)
    with pytest.raises(ValueError):
        Card.validate_params(4, 1)

    # Invalid rank
    with pytest.raises(ValueError):
        Card.validate_params(0, 0)
    with pytest.raises(ValueError):
        Card.validate_params(0, 14)
