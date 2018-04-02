from collections import Counter
import operator

STRAIGHT_FLUSH = "straight_flush"
FOUR_OF_A_KIND = "four_of_a_kind"
FULL_HOUSE = "full_house"
FLUSH = "flush"
STRAIGHT = "straight"
THREE_OF_A_KIND = "three_of_a_kind"
TWO_PAIR = "two_pair"
ONE_PAIR = "one_pair"
HIGH_CARD = "high_card"


class Card:
    num_ranking = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, card_str):
        self.number, self.suit = card_str[:-1], card_str[-1:]

    def __lt__(self, other):
        return Card.num_ranking.index(self.number) < Card.num_ranking.index(other.number)

    def __eq__(self, other):
        return Card.num_ranking.index(self.number) == Card.num_ranking.index(other.number)

    def __str__(self):
        return str("".join([self.number, self.suit]))


def get_unique_scores(scores_a, scores_b):
    uniques_a = [score for score in scores_a if score not in scores_b]
    uniques_b = [score for score in scores_b if score not in scores_a]

    return uniques_a, uniques_b


class Hand:
    hand_ranking = [HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND,
                    STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND,
                    STRAIGHT_FLUSH]

    def __init__(self, hand_str: str):
        self.hand = [Card(card_str) for card_str in hand_str.split()]
        self.highest_card = max(self.hand)
        self.scores = [Card.num_ranking.index(card.number) for card in self.hand]
        # Count number of occurences of each score
        self.score_counts = Counter(self.scores)

        self.single_scores = sorted([score for score, count in self.score_counts.items() if count == 1])
        self.pair_scores = sorted([score for score, count in self.score_counts.items() if count == 2])

    def __lt__(self, other):
        return Hand.hand_ranking.index(self.hand_type) < Hand.hand_ranking.index(other.hand_type)

    def __eq__(self, other):
        return Hand.hand_ranking.index(self.hand_type) == Hand.hand_ranking.index(other.hand_type)

    def __str__(self):
        return str(" ".join([str(card) for card in self.hand]))


    @property
    def hand_is_same_suit(self):
        return all(card == self.hand[0] for card in self.hand)


class HighCard(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = HIGH_CARD

    def __lt__(self, other):
        # If we are dealing with different hand patters, use the Hand
        # super class to make the comparison
        if other.__class__ != HighCard:
            return Hand.__lt__(self, other)

        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        if self_single_uniques and other_single_uniques:
            return max(self_single_uniques) < max(other_single_uniques)
        elif other_single_uniques:
            return True
        else:
            return False

    def __eq__(self, other):
        if other.__class__ != HighCard:
            return Hand.__eq__(self, other)

        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        return self_single_uniques == other_single_uniques == []


class OnePair(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = ONE_PAIR

    def __lt__(self, other):
        # If both aren't OnePair or if both aren't TwoPair:
        if other.__class__ != self.__class__:
            return Hand.__lt__(self, other)

        self_pair_uniques, other_pair_uniques = get_unique_scores(self.pair_scores, other.pair_scores)

        if self_pair_uniques and other_pair_uniques:
            return max(self_pair_uniques) < max(other_pair_uniques)
        elif other_pair_uniques:
            return True

        # Tie breaker with single cards
        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        if self_single_uniques and other_single_uniques:
            return max(self_single_uniques) < max(other_single_uniques)
        elif other_single_uniques:
            return True

        return False

    def __eq__(self, other):
        # If both aren't OnePair or if both aren't TwoPair:
        if other.__class__ != self.__class__:
            return Hand.__eq__(self, other)

        self_pair_uniques, other_pair_uniques = get_unique_scores(self.pair_scores, other.pair_scores)
        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        return (self_pair_uniques == other_pair_uniques == []) and (self_single_uniques == other_single_uniques)


class TwoPair(OnePair):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = TWO_PAIR


def get_hand_instance(hand_str):
    hand = [Card(card_str) for card_str in hand_str.split()]
    scores = [Card.num_ranking.index(card.number) for card in hand]
    # Count number of occurences of each score
    score_counts = Counter(scores)
    # Scores of available pairs
    pair_scores = sorted([score for score, count in score_counts.items() if count == 2])

    if len(pair_scores) == 2:
        return TwoPair(hand_str)
    elif len(pair_scores) == 1:
        return OnePair(hand_str)
    return HighCard(hand_str)


def best_hands(hands):
    hand_instances = [get_hand_instance(hand_str) for hand_str in hands]


    # Get highest hands
    # https://stackoverflow.com/a/21894160
    highest_hands = [hand_instances[i] for i, hand in enumerate(hand_instances) if hand == max(hand_instances)]

    return [str(hand) for hand in highest_hands]
