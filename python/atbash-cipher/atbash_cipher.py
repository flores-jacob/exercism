number_key = "1234567890"
base_key = "abcdefghijklmnopqrstuvwxyz"
plain_key = base_key + number_key
cipher_key = base_key[::-1] + number_key


def encode(plain_text):
    plain_text = filter(str.isalnum, plain_text.lower())

    cipher_text = []

    count = 0
    for i in plain_text:
        count += 1
        index = plain_key.index(i)
        cipher_text.append(cipher_key[index])
        if count % 5 == 0:
            cipher_text.append(' ')

    return "".join(cipher_text).strip()


def decode(ciphered_text):
    plain_text = []
    for char in ciphered_text:
        # use this instead so that we only need to go through the loop once
        if char.isspace():
            continue
        index = cipher_key.index(char)
        plain_text.append(plain_key[index])

    return "".join(plain_text)
