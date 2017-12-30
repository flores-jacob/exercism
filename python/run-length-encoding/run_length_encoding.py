from collections import deque

def decode(string):
    if not string:
        return ''

    decoded_string = ''

    string_deque = deque(list(string))

    while string_deque:
        current_character = string_deque.popleft()
        if current_character.isalpha():
            decoded_string += current_character
        elif current_character.isdigit():
            count = int(current_character)
            current_character = string_deque.popleft()
            decoded_string += current_character * count

    return decoded_string


def encode(string):
    encoded_string = ''

    string_list = list(string)
    previous_char = None
    current_count = 0
    for character in string_list:
        if not previous_char:
            current_count += 1
        elif character == previous_char:
            current_count += 1
        else:
            if current_count > 1:
                encoded_string = encoded_string + str(current_count)
            encoded_string = encoded_string + previous_char
            current_count = 1
        previous_char = character

    # append the final char and count
    if current_count > 1:
        encoded_string += str(current_count)
    encoded_string += previous_char

    return encoded_string