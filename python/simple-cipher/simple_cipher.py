class Cipher(object):
    base_key = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key="a"):
        index = Cipher.base_key.index(key)
        self.cipher_key = Cipher.base_key[index:] + Cipher.base_key[:index]

    def encode(self, text):
        cleaned_text = text.lower()
        cleaned_text = cleaned_text.replace(" ", "")
        encoded_char_list = [self.cipher_key[Cipher.base_key.index(char)] for char in cleaned_text if char in Cipher.base_key]

        return "".join(encoded_char_list)

    def decode(self, text):
        decoded_char_list = [Cipher.base_key[self.cipher_key.index(char)] for char in text if char in self.cipher_key]
        return "".join(decoded_char_list)

class Caesar(Cipher):
    def __init__(self):
        Cipher.__init__(self, "d")