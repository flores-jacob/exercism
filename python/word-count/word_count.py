def word_count(phrase):
    result_dict = {}
    words = phrase.split()
    for word in words:
        result_dict[word] = words.count(word)

    return result_dict
