def handshake(code):
    # https://stackoverflow.com/a/699891
    bin_str = "{0:b}".format(code)

    action_list = []

    for index, num in enumerate(reversed(bin_str)):
        if num == '1':
            if index == 0:
                action_list.append("wink")
            elif index == 1:
                action_list.append("double blink")
            elif index == 2:
                action_list.append("close your eyes")
            elif index == 3:
                action_list.append("jump")
            elif index == 4:
                action_list.reverse()
    return action_list


def secret_code(actions):
    vals = {"wink": int('1', 2),
            "double blink": int('10', 2),
            "close your eyes": int('100', 2),
            "jump": int('1000', 2)
            }

    total = 0

    for action in actions:
        total += vals[action]

    # Check if reversed
    # If the number of actions are more than one
    # And if the value of the first element is greater than the last
    # element, then the list is reversed, and we add b10,000
    if (len(actions) > 1) and (vals[actions[0]] > vals[actions[-1]]):
        total += int('10000', 2)

    return total
