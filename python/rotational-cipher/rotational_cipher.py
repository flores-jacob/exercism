def rotate(text, key):
    special_chars = ". ,'\"!?1234567890"
    plain_key_base = "abcdefghijklmnopqrstuvwxyz"
    cipher_key_base = plain_key_base[key:] + plain_key_base[:key]

    plain_key = plain_key_base + special_chars
    cipher_key = cipher_key_base + special_chars

    cipher_text = ""

    for char in text:
        lowered_char = char.lower()
        index = plain_key.index(lowered_char)
        if char.isupper():
            cipher_char = cipher_key[index].upper()
        else:
            cipher_char = cipher_key[index]
        cipher_text += cipher_char
    return cipher_text