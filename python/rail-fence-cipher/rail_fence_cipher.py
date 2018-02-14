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
    # Basically, we duplicate the encoding process using integers instead
    # Where the integers end up, represents the original position of each
    # element in the encoded message
    # Create a list of integers to encode
    rng = range(len(encoded_message))
    # Encode using the fence
    pos = fence_pattern(range(len(encoded_message)), rails)
    # Combine all elements in a single list
    pos = list(chain.from_iterable(pos))
    # Loop from 0 to len of message
    # Locate where the integer is in the encoded pos
    # Use the same index to pull the correct char from the encoded_message
    return ''.join(encoded_message[pos.index(n)] for n in rng)