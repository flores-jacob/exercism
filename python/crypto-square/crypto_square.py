from math import ceil

def encode(plain_text):
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    lower_case_text = plain_text.lower()

    normalized_text = "".join(letter for letter in lower_case_text if letter in valid_chars)

    message_length = len(normalized_text)

    square_root_of_length = message_length ** (1/2.0)

    column_size = ceil(square_root_of_length)



    return normalized_text.replace(" ", "")