def recite(start_verse, end_verse):
    if end_verse == 1:
        return ["On the first day of Christmas my true love gave to me, a Partridge in a Pear Tree."]

    verse_template = "On the {nth} day of Christmas my true love gave to me, {gifts}."

    gift_options = ["and a Partridge in a Pear Tree",
                    "two Turtle Doves",
                    "three French Hens",
                    "four Calling Birds",
                    "five Gold Rings",
                    "six Geese-a-Laying",
                    "seven Swans-a-Swimming",
                    "eight Maids-a-Milking",
                    "nine Ladies Dancing",
                    "ten Lords-a-Leaping",
                    "eleven Pipers Piping",
                    "twelve Drummers Drumming"]

    nth_day_list = ["first",
                    "second",
                    "third",
                    "fourth",
                    "fifth",
                    "sixth",
                    "seventh",
                    "eighth",
                    "ninth",
                    "tenth",
                    "eleventh",
                    "twelfth"]

    if start_verse == end_verse:
        # use nth_verse name to provide code clarity
        nth_verse = start_verse
        given_gifts_string = ", ".join(reversed(gift_options[:nth_verse]))
        verse = verse_template.format(nth=nth_day_list[nth_verse - 1], gifts=given_gifts_string)

        return [verse]
    else:
        return [recite(n, n)[0] for n in range(start_verse, end_verse + 1)]
