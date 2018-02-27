from itertools import combinations_with_replacement


def get_palindromes(max_factor, min_factor):
    factor_pairs = combinations_with_replacement(range(min_factor, max_factor + 1), 2)

    palindromes = {}

    for factor_pair in factor_pairs:
        pair_product = factor_pair[0] * factor_pair[1]
        # Check if the number reads the same forwards and backwards
        if str(pair_product) == str(pair_product)[::-1]:
            # If it does, add it to the dict
            if pair_product in palindromes:
                palindromes[pair_product].append((factor_pair[0], factor_pair[1]))
            else:
                palindromes[pair_product] = [(factor_pair[0], factor_pair[1])]

    return palindromes


def largest_palindrome(max_factor, min_factor):
    palindromes = (get_palindromes(max_factor, min_factor))
    final_palindrome_key = max(k for k, v in palindromes.items())

    return final_palindrome_key, palindromes[final_palindrome_key]


def smallest_palindrome(max_factor, min_factor):
    palindromes = (get_palindromes(max_factor, min_factor))
    first_palindrome_key = min(k for k, v in palindromes.items())

    return first_palindrome_key, palindromes[first_palindrome_key]
