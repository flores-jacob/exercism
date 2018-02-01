from math import ceil

def encode(plain_text):
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    lower_case_text = plain_text.lower()

    normalized_text = "".join(letter for letter in lower_case_text if letter in valid_chars)

    if not normalized_text:
        return ""

    message_length = len(normalized_text)

    square_root_of_length = message_length ** (1/2.0)

    column_size = int(ceil(square_root_of_length))

    row_size = int(ceil(message_length / column_size))

    row_elements = [[] for i in range(column_size)]
    for index, letter in enumerate(normalized_text):
        row_elements[index % column_size].append(letter)

    # Pad the last elements at the end with spaces
    for row in row_elements:
        if len(row) < column_size:
            row.extend(" " * (row_size - len(row)))

    return " ".join("".join(row) for row in row_elements)