import os, json
import collections


class Scrabble:

    def __init__(self):
        self.grid = [[None] * 8 for _ in range(8)]
        self.letters = [i % 26 for i in range(26 * 4)]


def main():
    pass


if __name__ == "__main__":
    main()