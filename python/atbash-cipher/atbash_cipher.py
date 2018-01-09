number_key = "1234567890"
base_key = "abcdefghijklmnopqrstuvwxyz"
plain_key = base_key + number_key
cipher_key = base_key[::-1] + number_key


def encode(plain_text):
    plain_text = filter(str.isalnum, plain_text.lower())

    cipher_text = ""

    count = 0
    for i in plain_text:
        count += 1
        index = plain_key.index(i)
        cipher_text += cipher_key[index]
        if count % 5 == 0:
            cipher_text += ' '

    return cipher_text.strip()


def decode(ciphered_text):
    pass
