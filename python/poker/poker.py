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
        # Scores of available pairs
        self.pair_scores = sorted([score for score, count in self.score_counts.items() if count == 2])

    def __lt__(self, other):
        return Hand.hand_ranking.index(self.hand_type) < Hand.hand_ranking.index(other.hand_type)

    def __eq__(self, other):
        return Hand.hand_ranking.index(self.hand_type) == Hand.hand_ranking.index(other.hand_type)

    def __str__(self):
        return str(" ".join([str(card) for card in self.hand]))

    @property
    def hand_type(self):
        max_score = max(self.score_counts.values())

        if len(self.pair_scores) == 2:
            return TWO_PAIR
        elif len(self.pair_scores) == 1:
            return ONE_PAIR
        else:
            return HIGH_CARD

    @property
    def hand_is_same_suit(self):
        return all(card == self.hand[0] for card in self.hand)

    def _lt_compare_same_hand_patterns(self, other):
        if self.hand_type != other.hand_type:
            raise ValueError("Cannot compare dissimilar hand types")

        if self.hand_type == ONE_PAIR == other.hand_type:
            # https://stackoverflow.com/a/268285
            self_pair_score = max(self.score_counts.items(), key=operator.itemgetter(1))[0]
            other_pair_score = max(other.score_counts.items(), key=operator.itemgetter(1))[0]

            return self_pair_score < other_pair_score

        elif self.hand_type == TWO_PAIR == other.hand_type:
            self_pair_uniques = [score for score in self.pair_scores if score not in other.pair_scores]
            other_pair_uniques = [score for score in other.pair_scores if score not in self.pair_scores]

            if self_pair_uniques and other_pair_uniques:
                return max(self_pair_uniques) < max(other_pair_uniques)
            elif other_pair_uniques:
                return True
            else:
                return False

        else:
            return False

    def _eq_compare_same_hand_patterns(self, other):
        if self.hand_type == ONE_PAIR == other.hand_type:
            self_pair_score = max(self.score_counts.items(), key=operator.itemgetter(1))[0]
            other_pair_score = max(other.score_counts.items(), key=operator.itemgetter(1))[0]

            return self_pair_score == other_pair_score

        elif self.hand_type == TWO_PAIR == other.hand_type:
            return self.pair_scores == other.pair_scores
        else:
            return False

    # def is_straight_flush(self):
    #     if self.hand_is_same_suit() and


class HighCard(Hand):
    def __lt__(self, other):
        # If we are dealing with different hand patters, use the Hand
        # super class to make the comparison
        if other.__class__ != HighCard:
            return super(HighCard, self).__lt__(other)

        self_uniques = [score for score in self.scores if score not in other.scores]
        other_uniques = [score for score in other.scores if score not in self.scores]

        if self_uniques and other_uniques:
            return max(self_uniques) < max(other_uniques)
        elif other_uniques:
            return True
        else:
            return False

    def __eq__(self, other):
        if other.__class__ != HighCard:
            return super(HighCard, self).__eq__(other)

        self_uniques = [score for score in self.scores if score not in other.scores]
        other_uniques = [score for score in other.scores if score not in self.scores]

        return self_uniques == other_uniques == []


class OnePair(Hand):
    pass

def best_hands(hands):
    for hand_str in hands:
        hand = HighCard(hand_str)
        # print(HighCard(hand_str) < HighCard(hand_str))

    hand_instances = [HighCard(hand_str) for hand_str in hands]


    # Get highest hands
    # https://stackoverflow.com/a/21894160
    highest_hands = [hand_instances[i] for i, hand in enumerate(hand_instances) if hand == max(hand_instances)]

    return [str(hand) for hand in highest_hands]