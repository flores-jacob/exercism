def detect_anagrams(word, candidates):
    anagram_list =[]
    letter_sorted_word = sorted(word.lower())
    for candidate in candidates:
        candidate_sorted_word = sorted(candidate.lower())
        if candidate_sorted_word == letter_sorted_word:
            if word.lower() != candidate.lower():
                anagram_list.append(candidate)

    return anagram_list
