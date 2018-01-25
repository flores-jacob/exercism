class Cipher(object):
    base_key = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key="a"):
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
        decoded_char_list = [Cipher.base_key[self.cipher_key.index(char)] for char in text if char in self.cipher_key]

        return "".join(decoded_char_list)


class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, "d")



# print(Cipher(key="aadd").encode("aaaa"))