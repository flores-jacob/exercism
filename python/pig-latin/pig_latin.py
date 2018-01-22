def translate(text):
    split_text = text.split()

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    two_letter_special_cases = ["ch", "qu", "th"]
    xr_yt_special_cases = ["xr", "yt"]
    three_letter_special_cases = ["thr", "sch"]

    return_text = ""

    for word in split_text:
        word = word.lower()
        if (word[0] in consonants) and (word[1:3] == "qu"):
            return_text += (word[3:] + word[0:3] + "ay")
        elif word[0:3] in three_letter_special_cases:
            return_text += word[3:] + word[0:3] + "ay"
        elif word[0:2] in two_letter_special_cases:
            return_text += (word[2:] + word[0:2] + "ay")
        elif word[0:2] in xr_yt_special_cases:
            return_text += (word + "ay")
        elif word[0] in vowels:
            return_text += (word + "ay")
        elif word[0] in consonants:
            return_text += (word[1:] + word[0] + "ay")

    return return_text