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
    pass
