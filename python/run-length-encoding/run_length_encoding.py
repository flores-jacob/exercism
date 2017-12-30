from collections import OrderedDict

def decode(string):
    pass


def encode(string):
    encoded_string = ''
    character_dict = OrderedDict()

    string_list = list(string)
    for character in string_list:
        if character in character_dict.keys():
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    for character_key in character_dict:
        count = character_dict[character_key]
        if count > 1:
            encoded_string += str(count)
        encoded_string += character_key

    return encoded_string
