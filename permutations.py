"""
Permutations
link: https://www.codewars.com/kata/5254ca2719453dcc0b00027d
In this kata you have to create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""


def permutations(args):
    alphabet = list(args)
    word_len = len(args)

    mutants = next_gen('', alphabet, word_len)
    return mutants


def next_gen(old_gen, alphabet, word_len):
    new_gens = []
    for i in alphabet:
        new_gen = old_gen + i
        if len(new_gen) == word_len:
            new_gens.append(new_gen)
        new_alphabet = alphabet.copy()
        new_alphabet.remove(i)

        if new_alphabet:
            new_gens.extend(next_gen(new_gen, new_alphabet, word_len))

    return list(set(new_gens))


def main():
    permutations('a')
    # ['a']
    permutations('ab')
    # ['ab', 'ba']
    permutations('aabb')
    # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


if __name__ == "__main__":
    main()
