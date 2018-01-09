def abbreviate(words):
    words = words.replace('-', ' ')
    word_list = words.split()

    acronym_letter_list = [word[0].upper() for word in word_list]

    return "".join(acronym_letter_list)
