import os, json
import collections
from enum import Enum
import random


class Suite(Enum):
    HEARTS = 1,
    CLUBS = 2,
    DIAMONDS = 3,
    SPADES = 4


class PlayerStatus(Enum):
    WON = 1,
    BUSTED = 2,
    IN_GAME = 3


class Card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite


class BlackJack:
    def __init__(self, users):
        self.cards = []
        self.card_reset()
        self.shuffle()
        self.players = {user: [] for user in users}
        self.dealer = []
        self.player_stand = {user: False for user in users}

    def shuffle(self):
        # reservoir sampling
        # fisher yates algorithm
        n = 52
        for i in range(52):
            random_number = random.randint(0, n - i - 1)
            self.cards[n - 1 - i], self.cards[random_number] = self.cards[random_number], self.cards[n - 1 - i]

        # [1, 2, 3 ,4]
        # [1, 4, 3,] 2
        # [3, 4], 1, 2
        # [3], 4, 1, 2

    def card_reset(self):
        self.cards.clear()
        for suite in (Suite.CLUBS, Suite.DIAMONDS, Suite.HEARTS, Suite.SPADES):
            for num in range(1, 14):
                self.cards.append(Card(num, suite))

    def did_player_win(self, player):
        curr_count = self.get_player_count(player)
        print(f"{player}  {curr_count}")
        if curr_count == 21:
            return PlayerStatus.WON
        if curr_count > 21:
            return PlayerStatus.BUSTED
        return PlayerStatus.IN_GAME

    def deal(self):
        # dealer deal
        self.dealer.append(self.cards.pop())
        self.dealer.append(self.cards.pop())
        for player in self.players.keys():
            self.players[player].append(self.cards.pop())
            if self.did_player_win(player) == PlayerStatus.WON:
                print(f"{player} Won!")
                return

    def hit(self, player):
        if self.player_stand[player]:
            print("No CHeating , player has stood")
            return
        self.players[player].append(self.cards.pop())
        player_status = self.did_player_win(player)
        if player_status == PlayerStatus.WON:
            print(f"{player} Won!")
        if player_status == PlayerStatus.IN_GAME:
            print(f"{player} In Game")
        if player_status == PlayerStatus.BUSTED:
            print(f"{player} Busted")
            self.player_stand[player] = True

    def get_player_count(self, player):
        pcards = self.players[player]
        return self.card_count(pcards)

    def card_count(self, pcards):
        pcards.sort(key=lambda x: x.number)
        curr_count = 0
        for card in reversed(pcards):
            if card.number == 1:
                if curr_count + 11 > 21:
                    curr_count += 1
                else:
                    curr_count += 11
            elif 10 <= card.number <= 13:
                curr_count += 10
            else:
                curr_count += card.number

        return curr_count

    def stand(self, player):
        self.player_stand[player] = True
        if all(self.player_stand.values()):
            print(f"Dealer Card Count {self.card_count(self.dealer)}")
            if self.card_count(self.dealer) > 21:
                print(f"Dealer busted")
            elif self.card_count(self.dealer) == 21:
                print("Dealer Won")
            else:
                print("Dealer lost")


if __name__ == "__main__":
    b = BlackJack(["Deepu", "Doofu"])
    b.deal()
    b.hit("Deepu")
    b.hit("Doofu")
    b.hit("Deepu")
    b.hit("Doofu")
    b.stand("Deepu")
    b.stand("Doofu")