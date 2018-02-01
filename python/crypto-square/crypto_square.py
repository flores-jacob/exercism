from math import ceil, sqrt


def encode(plain_text):
    normalized_text = "".join(letter.lower() for letter in plain_text if letter.isalnum())

    if not normalized_text:
        return ""

    column_size = int(ceil(sqrt(len(normalized_text))))
    row_size = int(ceil(len(normalized_text)/column_size))

    row_elements = [[] for i in range(column_size)]
    for index, letter in enumerate(normalized_text):
        row_elements[index % column_size].append(letter)

    # Pad the last elements at the end with spaces
    for row in row_elements:
        if len(row) < column_size:
            row.extend(" " * (row_size - len(row)))

    return " ".join("".join(row) for row in row_elements)