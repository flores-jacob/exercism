def is_pangram(sentence):
    sentence = sentence.lower()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in alphabet:
        if sentence.count(char) == 0:
            return False

    return True
