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


class Hand:
    hand_ranking = [HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND,
                    STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND,
                    STRAIGHT_FLUSH]

    def __init__(self, hand_str: str):
        self.hand = [Card(card_str) for card_str in hand_str.split()]
        self.highest_card = max(self.hand)
        self.scores = [Card.num_ranking.index(card.number) for card in self.hand]

    def __lt__(self, other):
        if Hand.hand_ranking.index(self.hand_type) < Hand.hand_ranking.index(other.hand_type):
            return True
        elif Hand.hand_ranking.index(self.hand_type) == Hand.hand_ranking.index(other.hand_type):
            return self._lt_compare_same_hand_patterns(other)

        else:
            return False

    def __eq__(self, other):
        return self._eq_compare_same_hand_patterns(other)

    def __str__(self):
        return str(" ".join([str(card) for card in self.hand]))

    @property
    def hand_type(self):
        # Count number of occurences of each score
        score_counts = Counter(self.scores)

        print("score_counts",score_counts)

        max_score = max(score_counts.values())

        if max_score == 2:
            return ONE_PAIR
        else:
            return HIGH_CARD

    @property
    def hand_is_same_suit(self):
        return all(card == self.hand[0] for card in self.hand)

    def _lt_compare_same_hand_patterns(self, other):
        if self.hand_type != other.hand_type:
            raise ValueError("Cannot compare dissimilar hand types")

        if self.hand_type == HIGH_CARD == other.hand_type:
            self_uniques = [score for score in self.scores if score not in other.scores]
            other_uniques = [score for score in other.scores if score not in self.scores]

            if self_uniques and other_uniques:
                return max(self_uniques) < max(other_uniques)
            elif other_uniques:
                return True
            else:
                return False

    def _eq_compare_same_hand_patterns(self, other):
        if Hand.hand_ranking.index(self.hand_type) != Hand.hand_ranking.index(other.hand_type):
            raise ValueError("Cannot compare dissimilar hand types")

        if self.hand_type == HIGH_CARD == other.hand_type:
            self_uniques = [score for score in self.scores if score not in other.scores]
            other_uniques = [score for score in other.scores if score not in self.scores]

            return self_uniques == other_uniques

    # def is_straight_flush(self):
    #     if self.hand_is_same_suit() and


def best_hands(hands):
    for hand_str in hands:
        hand = Hand(hand_str)
        print(hand)

    hand_instances = [Hand(hand_str) for hand_str in hands]

    # Get highest hands
    # https://stackoverflow.com/a/21894160
    highest_hands = [hand_instances[i] for i, hand in enumerate(hand_instances) if hand == max(hand_instances)]

    return [str(hand) for hand in highest_hands]