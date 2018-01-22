def translate(text):
    split_text = text.split()

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    two_letter_special_cases = ["ch", "qu", "th"]
    xr_yt_special_cases = ["xr", "yt"]
    three_letter_special_cases = ["thr", "sch"]

    return_text = []

    for word in split_text:
        word = word.lower()
        if (word[0] in consonants) and (word[1:3] == "qu"):
            return_text.append(word[3:] + word[0:3] + "ay")
        elif word[0:3] in three_letter_special_cases:
            return_text.append(word[3:] + word[0:3] + "ay")
        elif word[0:2] in two_letter_special_cases:
            return_text.append(word[2:] + word[0:2] + "ay")
        elif word[0:2] in xr_yt_special_cases:
            return_text.append(word + "ay")
        elif word[0] in vowels:
            return_text.append(word + "ay")
        elif word[0] == "y":
            return_text.append(word[1:] + "yay")
        elif word[0] in consonants:
            # identify initial consonant cluster
            consonant_cluster = ""
            for letter in word:
                if (letter not in vowels) and (letter != "y"):
                    consonant_cluster += letter
                else:
                    break

            return_text.append(word[len(consonant_cluster):] + consonant_cluster + "ay")

    return " ".join(return_text)