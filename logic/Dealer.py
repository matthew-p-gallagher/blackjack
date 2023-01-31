import os
import sys

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from logic.Hand import Hand


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def reset(self):
        self.hand.reset()
