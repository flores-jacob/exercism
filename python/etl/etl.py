from collections import defaultdict


def transform(legacy_data):
    new_data = defaultdict()

    for score, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = score

    return new_data
