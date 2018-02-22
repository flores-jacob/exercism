def generate_generic_verse(verse_number):
    return (["{} bottles of beer on the wall, {} bottles of beer.".format(verse_number, verse_number),
             "Take one down and pass it around, {} bottles of beer on the wall.".format(verse_number - 1)])


def recite(start, take=1):
    song = generate_generic_verse(start)
    print(song)
    return (song)
