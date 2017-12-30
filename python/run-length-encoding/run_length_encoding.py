from collections import OrderedDict

def decode(string):
    pass


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


# mystring = encode('AABBBCCCC'), '2A3B4C'