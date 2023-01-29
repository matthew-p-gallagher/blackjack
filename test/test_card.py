import pytest

from Card import Card


def test_card_init():
    # Ace
    card = Card(0, 1)
    assert card.suit == 0
    assert card.rank == 1
    assert card.soft
    assert card.score == 11
    assert card.img_path == "images\\0_1.png"

    # Jack
    card = Card(1, 11)
    assert card.suit == 0
    assert card.rank == 11
    assert not card.soft
    assert card.score == 10
    assert card.img_path == "images\\1_11.png"

    # King
    card = Card(2, 13)
    assert card.suit == 0
    assert card.rank == 13
    assert not card.soft
    assert card.score == 10
    assert card.img_path == "images\\2_13.png"

    # Number card
    card = Card(3, 5)
    assert card.suit == 0
    assert card.rank == 5
    assert not card.soft
    assert card.score == 5
    assert card.img_path == "images\\3_5.png"


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
