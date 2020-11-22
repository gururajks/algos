import os, json
import collections
from enum import Enum
import random

# there are 52 cards
from typing import List


class CardType(Enum):
    HEART = (0, "Hearts")
    SPADE = (1, "Spade")
    DIAMOND = (2, "Diamond")
    CLUBS = (3, "Clubs")


class Card:
    def __init__(self, number, face_value):
        self.number = number
        self.face_value = face_value

    def __str__(self):
        return "{}   {}".format(self.number, self.face_value)


class Deck:
    def __init__(self):
        self.cards = []
        for cardType in CardType:
            for i in range(1, 14):
                self.cards.append(Card(i, cardType))

    def shuffle(self):
        for i in range(52):
            swap_idx = random.randint(0, 51)
            self.cards[i], self.cards[swap_idx] = self.cards[swap_idx], self.cards[i]

    def pick(self):
        return self.cards.pop()

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)


class Player:

    def __init__(self, name, amount):
        self.name = name
        self.cards = []
        self.amount = amount


class Poker:
    def __init__(self, players: List[Player]):
        self.d = Deck()
        self.d.shuffle()
        self.players = players
        self.community = []
        self.pot = 0

    def distribute(self) -> None:
        for player in self.players:
            player.cards = [self.d.pick(), self.d.pick()]

    def flop(self):
        self.community = [self.d.pick(), self.d.pick(), self.d.pick()]

    def turn(self):
        self.community.append(self.d.pick())

    def river(self):
        self.turn()

    def play(self):
        self.distribute()
        self.flop()
        self.turn()
        self.river()
        for card in self.community:
            print(card)




if __name__ == "__main__":
    p = Poker([Player("Deepu", 20), Player("Doofu", 10), Player("Doofy", 15)])
    p.play()
