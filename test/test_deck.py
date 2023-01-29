import pytest

from Deck import Deck
from Card import Card


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def unshuffled():
    return "010203040506070809010011012013111213141516171819110111112113212223242526272829210211212213313233343536373839310311312313"


def test_deck_init(deck, unshuffled):
    assert deck.no_of_cards() == 52

    for suit in range(4):
        for rank in range(1, 14):
            card = Card(suit, rank)
            assert card in deck.cards

    assert deck.encoded != unshuffled


def test_deck_shuffle(deck):
    encoded_before = deck.encoded
    size_before = deck.no_of_cards()
    deck.shuffle()
    assert deck.no_of_cards() == size_before
    assert deck.encoded != encoded_before
    assert deck.encoded != unshuffled


def test_deal_success(deck):
    size_before = deck.no_of_cards()
    card = deck.deal()
    assert card not in deck.cards
    assert deck.no_of_cards() == size_before - 1


def test_deal_no_cards(deck):
    deck.cards = []
    assert deck.deal() is None


def test_reset(deck):
    deck.reset()
    assert deck.no_of_cards() == 52

    for suit in range(4):
        for rank in range(1, 14):
            card = Card(suit, rank)
            assert card in deck.cards
