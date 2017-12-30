def hey(phrase):

    phrase = phrase.strip()

    if not phrase:
        return "Fine. Be that way!"

    if phrase.isupper():
        return "Whoa, chill out!"

    if phrase[-1] == "?":
        return "Sure."

    return "Whatever."
