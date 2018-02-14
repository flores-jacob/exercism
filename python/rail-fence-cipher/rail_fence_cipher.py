from collections import deque


def fence_pattern(rails, message_size):
    pass


def encode(rails, message):
    deque_list = [deque() for i in range(message)]

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

        if count == message - 1:
            direction = "up"
        elif count == 0:
            direction = "down"

    return "".join(["".join(deque_item) for deque_item in deque_list])


def decode(rails, encoded_message):
    pass