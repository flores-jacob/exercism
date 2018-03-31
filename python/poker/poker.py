from typing import List


class Card:
    num_ranking = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_str):
        self.number, self.suit = card_str[:-1], card_str[-1:]

    def __cmp__(self, other):
        if Card.num_ranking.index(self.number) > Card.num_ranking.index(other.number):
            return 1
        elif Card.num_ranking.index(self.number) < Card.num_ranking.index(other.number):
            return -1
        else:
            return 0

    def __str__(self):
        return str((self.number, self.suit))


class Hand:
    def __init__(self, hand_str: str):
        self.hand = [Card(card_str) for card_str in hand_str.split()]

    def __str__(self):
        return str([str(card) for card in self.hand])


def check_straight_flush(hand: List[str]) -> bool:
    pass


def best_hands(hands):
    for hand_str in hands:
        hand = Hand(hand_str)
        print(hand)

    if len(hands) == 1:
        return hands
