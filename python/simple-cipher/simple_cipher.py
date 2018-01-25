import random


class Cipher(object):
    base_key = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key=None):
        if not key:
            key_generator = random.Random()
            key_char_list = [key_generator.choice(Cipher.base_key) for i in range(random.randint(100, 200))]
            key = "".join(key_char_list)
        elif not all(char.isalpha() and char.islower()for char in key):
            raise ValueError("Invalid characters")

        self.key = key

    def encode(self, text):
        cleaned_text = text.lower()
        cleaned_text = cleaned_text.replace(" ", "")

        encoded_char_list = []

        key_length = len(self.key)

        for i in range(len(cleaned_text)):

            index = Cipher.base_key.index(self.key[i % key_length])
            cipher_key = Cipher.base_key[index:] + Cipher.base_key[:index]

            if cleaned_text[i] in Cipher.base_key:
                encoded_char_list.append(cipher_key[Cipher.base_key.index(cleaned_text[i])])

        return "".join(encoded_char_list)

    def decode(self, text):
        decoded_char_list = []

        key_length = len(self.key)

        for i in range(len(text)):

            index = Cipher.base_key.index(self.key[i % key_length])
            cipher_key = Cipher.base_key[index:] + Cipher.base_key[:index]

            if text[i] in Cipher.base_key:
                decoded_char_list.append(Cipher.base_key[cipher_key.index(text[i])])

        return "".join(decoded_char_list)


class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, "d")
