import pytest

from Card import Card
from Deck import Deck

from Hand import Hand


@pytest.fixture
def deck():
    return Deck()


@pytest.fixture
def hand():
    return Hand()


@pytest.fixture
def ace_of_hearts():
    return Card(0, 1)


def test_hand_init(hand):
    assert hand.cards == []
    assert hand.score == 0
    assert hand.soft == False
    assert hand.bust == False
    assert hand.blackjack == False


def test_add_first_card_general(hand, deck):
    card = deck.deal()
    hand.add_card(card)
    assert hand.cards == [card]
    assert hand.score == card.score
    assert hand.soft == card.soft
    assert hand.bust == False
    assert hand.blackjack == False


def test_add_second_card_general(hand, deck):
    card1 = deck.deal()
    card2 = deck.deal()
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == card1.score + card2.score
    assert hand.soft == card1.soft or card2.soft
    assert hand.bust == False


def test_add_num_num(hand, deck):
    card1 = Card(0, 5)
    card2 = Card(1, 6)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 11
    assert hand.soft == False
    assert hand.bust == False


def test_add_ace_number(hand, deck):
    card1 = Card(0, 1)
    card2 = Card(0, 5)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 16
    assert hand.soft == True
    assert hand.bust == False


def test_add_ace_ace(hand, deck):
    card1 = Card(0, 1)
    card2 = Card(1, 1)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 12
    assert hand.soft == True
    assert hand.bust == False


def test_add_ace_face(hand, deck):
    card1 = Card(0, 1)
    card2 = Card(1, 12)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 21
    assert hand.soft == True
    assert hand.bust == False


def test_add_face_face(hand, deck):
    card1 = Card(0, 12)
    card2 = Card(1, 11)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 20
    assert hand.soft == False
    assert hand.bust == False


def test_add_many_and_bust(hand, deck):
    card1 = Card(0, 5)
    card2 = Card(0, 6)
    card3 = Card(1, 5)
    card4 = Card(1, 3)
    card5 = Card(2, 9)
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)
    hand.add_card(card4)
    hand.add_card(card5)
    assert hand.cards == [card1, card2, card3, card4, card5]
    assert hand.score == 28
    assert hand.soft == False
    assert hand.bust == True


def test_add_soft_saves_bust(hand, deck):
    card1 = Card(0, 5)
    card2 = Card(1, 1)
    card3 = Card(1, 7)
    hand.add_card(card1)
    hand.add_card(card2)
    assert hand.cards == [card1, card2]
    assert hand.score == 16
    assert hand.soft == True
    assert hand.bust == False
    hand.add_card(card3)
    hand.remove_soft()
    assert hand.cards == [card1, card2, card3]
    assert hand.score == 13
    assert hand.soft == False
    assert hand.bust == False
