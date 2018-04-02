from collections import Counter

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


def hand_is_straight(scores):
    scores = sorted(scores)
    diff1 = (scores[0] - scores[1]) == -1
    diff2 = (scores[0] - scores[2]) == -2
    diff3 = (scores[0] - scores[3]) == -3
    diff4 = (scores[0] - scores[4]) == -4

    # 2(0pts) 3(1pts) 4(2pts) 5(3pts) A(12pts)
    diff5 = scores[0] - scores[4] == -12

    return diff1 and diff2 and diff3 and (diff4 or diff5)


class Hand:
    hand_ranking = [HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND,
                    STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND,
                    STRAIGHT_FLUSH]

    def __init__(self, hand_str: str):
        self.hand = [Card(card_str) for card_str in hand_str.split()]
        self.scores = [Card.num_ranking.index(card.number) for card in self.hand]
        # Count number of occurrences of each score
        self.score_counts = Counter(self.scores)

        self.single_scores = sorted([score for score, count in self.score_counts.items() if count == 1])
        self.pair_scores = sorted([score for score, count in self.score_counts.items() if count == 2])
        self.threes_scores = sorted([score for score, count in self.score_counts.items() if count == 3])
        self.fours_scores = sorted([score for score, count in self.score_counts.items() if count == 4])

    def __lt__(self, other):
        return Hand.hand_ranking.index(self.hand_type) < Hand.hand_ranking.index(other.hand_type)

    def __eq__(self, other):
        return Hand.hand_ranking.index(self.hand_type) == Hand.hand_ranking.index(other.hand_type)

    def __str__(self):
        return str(" ".join([str(card) for card in self.hand]))

    def _lt_singles(self, other):
        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        if self_single_uniques and other_single_uniques:
            return max(self_single_uniques) < max(other_single_uniques)
        elif other_single_uniques:
            return True
        else:
            return False

    def _lt_pairs(self, other):
        self_pair_uniques, other_pair_uniques = get_unique_scores(self.pair_scores, other.pair_scores)

        if self_pair_uniques and other_pair_uniques:
            return max(self_pair_uniques) < max(other_pair_uniques)
        elif other_pair_uniques:
            return True
        else:
            # Tie breaker with single cards
            return self._lt_singles(other)

    def _lt_threes(self, other):
        self_threes_uniques, other_threes_uniques = get_unique_scores(self.threes_scores, other.threes_scores)

        if self_threes_uniques and other_threes_uniques:
            return max(self_threes_uniques) < max(other_threes_uniques)
        elif other_threes_uniques:
            return True
        else:
            # Tie breaker with pair cards
            return self._lt_pairs(other)

    def _lt_fours(self, other):
        self_fours_uniques, other_fours_uniques = get_unique_scores(self.fours_scores, other.fours_scores)

        if self_fours_uniques and other_fours_uniques:
            return max(self_fours_uniques) < max(other_fours_uniques)
        elif other_fours_uniques:
            return True
        else:
            # Tie breaker with single card
            return self._lt_singles(other)

    def _eq_singles(self, other):
        self_single_uniques, other_single_uniques = get_unique_scores(self.single_scores, other.single_scores)

        return self_single_uniques == other_single_uniques == []

    def _eq_pairs(self, other):
        self_pair_uniques, other_pair_uniques = get_unique_scores(self.pair_scores, other.pair_scores)

        return (self_pair_uniques == other_pair_uniques == []) and self._eq_singles(other)

    def _eq_threes(self, other):

        self_threes_uniques, other_threes_uniques = get_unique_scores(self.threes_scores, other.threes_scores)

        return (self_threes_uniques == other_threes_uniques == []) and self._eq_pairs(other)

    def _eq_fours(self, other):

        self_fours_uniques, other_fours_uniques = get_unique_scores(self.fours_scores, other.fours_scores)

        return (self_fours_uniques == other_fours_uniques == []) and self._eq_singles(other)


class HighCard(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = HIGH_CARD

    def __lt__(self, other):
        # If we are dealing with different hand patters, use the Hand
        # super class to make the comparison
        if other.__class__ != HighCard:
            return Hand.__lt__(self, other)

        return self._lt_singles(other)

    def __eq__(self, other):
        if other.__class__ != HighCard:
            return Hand.__eq__(self, other)

        return self._eq_singles(other)


class OnePair(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = ONE_PAIR

    def __lt__(self, other):
        # If both aren't OnePair or if both aren't TwoPair:
        if other.__class__ != self.__class__:
            return Hand.__lt__(self, other)

        return self._lt_pairs(other)

    def __eq__(self, other):
        # If both aren't OnePair or if both aren't TwoPair:
        if other.__class__ != self.__class__:
            return Hand.__eq__(self, other)

        return self._eq_pairs(other)


class TwoPair(OnePair):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = TWO_PAIR


class ThreeOfAKind(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = THREE_OF_A_KIND

    def __lt__(self, other):
        if other.__class__ != ThreeOfAKind:
            return Hand.__lt__(self, other)

        return self._lt_threes(other)

    def __eq__(self, other):
        if other.__class__ != ThreeOfAKind:
            return Hand.__eq__(self, other)

        return self._eq_threes(other)


class Straight(Hand):
    def __init__(self, hand_str: str):
        super().__init__(hand_str)
        self.hand_type = STRAIGHT

        # If the last element is one more than the penultimate one, then
        # the last element is the highest card
        if self.single_scores[-1] - self.single_scores[-2] == 1:
            self.straight_high = self.single_scores[-1]
        # if the last element is greater than the penultimate one by more
        # than one, then the last element is probably the ace which has a
        # score of 12, and the penultimate element is 5, and the pattern
        # is A 2 3 4 5, with 5 as the high card
        else:
            self.straight_high = self.single_scores[-2]

    def __lt__(self, other):
        if other.__class__ != self.__class__:
            return Hand.__lt__(self, other)

        return self.straight_high < other.straight_high

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            return Hand.__eq__(self, other)

        return self.straight_high == other.straight_high


class Flush(Hand):
    def __init__(self, hand_str):
        super().__init__(hand_str)
        self.hand_type = FLUSH

    def __lt__(self, other):
        if other.__class__ != Flush:
            return Hand.__lt__(self, other)

        return self._lt_singles(other)

    def __eq__(self, other):
        if other.__class__ != Flush:
            return Hand.__eq__(self, other)

        return self._eq_singles(other)


class FullHouse(Hand):
    def __init__(self, hand_str):
        super().__init__(hand_str)
        self.hand_type = FULL_HOUSE

    def __lt__(self, other):
        if other.__class__ != FullHouse:
            return Hand.__lt__(self, other)

        return self._lt_threes(other)

    def __eq__(self, other):
        if other.__class__ != FullHouse:
            return Hand.__eq__(self, other)

        return self._eq_threes(other)


class FourOfAKind(Hand):
    def __init__(self, hand_str):
        super().__init__(hand_str)
        self.hand_type = FOUR_OF_A_KIND

    def __lt__(self, other):
        if other.__class__ != FourOfAKind:
            return Hand.__lt__(self, other)

        return self._lt_fours(other)

    def __eq__(self, other):
        if other.__class__ != FourOfAKind:
            return Hand.__eq__(self, other)

        return self._eq_fours(other)


class StraightFlush(Straight):
    def __init__(self, hand_str):
        super().__init__(hand_str)
        self.hand_type = STRAIGHT_FLUSH


def get_hand_instance(hand_str):
    hand = [Card(card_str) for card_str in hand_str.split()]
    individual_scores = [Card.num_ranking.index(card.number) for card in hand]
    # Count number of occurrences of each score
    score_counts = Counter(individual_scores)
    # Scores of available pairs
    pair_scores = sorted([score for score, count in score_counts.items() if count == 2])
    triple_scores = sorted([score for score, count in score_counts.items() if count == 3])
    quad_scores = sorted([score for score, count in score_counts.items() if count == 4])

    all_suits_the_same = all(card.suit == hand[0].suit for card in hand)

    if hand_is_straight(individual_scores) and all_suits_the_same:
        return StraightFlush(hand_str)
    elif len(quad_scores) == 1:
        return FourOfAKind(hand_str)
    elif (len(triple_scores) == 1) and (len(pair_scores) == 1):
        return FullHouse(hand_str)
    elif all_suits_the_same:
        return Flush(hand_str)
    elif hand_is_straight(individual_scores):
        return Straight(hand_str)
    elif len(triple_scores) == 1:
        return ThreeOfAKind(hand_str)
    elif len(pair_scores) == 2:
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
