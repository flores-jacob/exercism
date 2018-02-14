from collections import deque
from itertools import chain


def fence_pattern(rails, message_size):
    """
    :param rails: string or iterable to be put on rails
    :param message_size: length of the string or iterable
    :return: a list of deques that have been put on the rail
    """
    deque_list = [deque() for i in range(message_size)]

    rails = deque(rails)
    direction = "down"
    count = 0
    while rails:
        mychar = rails.popleft()
        deque_list[count].append(mychar)
        if direction == "down":
            count += 1
        elif direction == "up":
            count -= 1

        if count == message_size - 1:
            direction = "up"
        elif count == 0:
            direction = "down"

    return deque_list


def encode(message, rails):
    """
    :param message: String that needs to be encoded
    :param rails: The number of rails
    :return: String of encoded message
    """
    fence = fence_pattern(message, rails)
    return "".join(["".join(deque_item) for deque_item in fence])


def decode(encoded_message, rails):
    # decode solution adapted from https://stackoverflow.com/a/14520203
    rng = range(len(encoded_message))
    pos = fence_pattern(range(len(encoded_message)), rails)
    pos = list(chain.from_iterable(pos))
    return ''.join(encoded_message[pos.index(n)] for n in rng)