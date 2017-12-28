def word_count(phrase):

    trans_dict = phrase.maketrans(',:!@$%^&._', '          ')
    phrase = phrase.translate(trans_dict).lower()

    result_dict = {}
    words = phrase.split()
    words = [word.strip("'") for word in words]
    for word in words:
        result_dict[word] = words.count(word)

    return result_dict
