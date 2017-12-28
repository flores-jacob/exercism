def word_count(phrase):
    phrase = phrase.replace(',', ' ')

    print (phrase)

    result_dict = {}
    words = phrase.split()
    for word in words:
        result_dict[word] = words.count(word)

    return result_dict
