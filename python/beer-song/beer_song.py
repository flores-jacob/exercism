def generate_generic_verse(verse_number):
    return (["{} bottles of beer on the wall, {} bottles of beer.".format(verse_number, verse_number),
             "Take one down and pass it around, {} bottles of beer on the wall.".format(verse_number - 1)])


def recite(start, take=1):
    verses = []

    for i in range(take):
        if start >= 3:
            verses.extend(generate_generic_verse(start))
        elif start == 2:
            verses.extend(["2 bottles of beer on the wall, 2 bottles of beer.",
                           "Take one down and pass it around, 1 bottle of beer on the wall."])
        elif start == 1:
            verses.extend(["1 bottle of beer on the wall, 1 bottle of beer.",
                           "Take it down and pass it around, no more bottles of beer on the wall."])
        elif start == 0:
            verses.extend(["No more bottles of beer on the wall, no more bottles of beer.",
                           "Go to the store and buy some more, 99 bottles of beer on the wall."])
        # Append an empty string in between verses
        verses.append("")
        start -= 1

    # Make sure to exclude the final empty string when returning the list of
    # verses
    return verses[:-1]
