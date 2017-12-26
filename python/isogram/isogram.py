def is_isogram(string):
    is_isogram = True

    string = string.lower()

    for letter in string:
        if (letter != "-") and (letter != ' '):
            if string.count(letter) > 1:
                is_isogram = False

    return is_isogram
