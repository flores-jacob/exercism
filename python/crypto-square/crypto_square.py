def encode(plain_text):
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    lower_case_text = plain_text.lower()

    normalized_text = "".join(letter for letter in lower_case_text if letter in valid_chars)

    return normalized_text