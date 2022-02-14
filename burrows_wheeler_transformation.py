"""
Burrows-Wheeler-Transformation
link: https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb
Motivation
When compressing sequences of symbols, it is useful to have many equal symbols follow each other, because then they
can be encoded with a run length encoding.
For example, RLE encoding of "aaaabbbbbbbbbbbcccccc" would give something like 4a 11b 6c.

(Look here for learning more about the run-length-encoding.)

Of course, RLE is interesting only if the string contains many identical consecutive characters.
But what bout human readable text? Here comes the Burrows-Wheeler-Transformation.

Transformation
There even exists a transformation, which brings equal symbols closer together,
it is called the Burrows-Wheeler-Transformation.
The forward transformation works as follows:
Let's say we have a sequence with length n, first write every shift of that string into a n x n matrix:

Input: "bananabar"

b a n a n a b a r
r b a n a n a b a
a r b a n a n a b
b a r b a n a n a
a b a r b a n a n
n a b a r b a n a
a n a b a r b a n
n a n a b a r b a
a n a n a b a r b
Then we sort that matrix by its rows.
The output of the transformation then is the last column and the row index in which the original string is in:

               .-.
a b a r b a n a n
a n a b a r b a n
a n a n a b a r b
a r b a n a n a b
b a n a n a b a r <- 4
b a r b a n a n a
n a b a r b a n a
n a n a b a r b a
r b a n a n a b a
               '-'

Output: ("nnbbraaaa", 4)
Of course we want to restore the original input, therefore you get the following hints:

The output contains the last matrix column.
The first column can be acquired by sorting the last column.
For every row of the table: Symbols in the first column follow on symbols in the last column,
in the same way they do in the input string.
You don't need to reconstruct the whole table to get the input back.
"""


import unittest


def get_shift_right(string, i):
    return "".join((string[-i:], string[:-i]))


def get_all_shifts(string):
    shifts = []
    for i in range(0, len(string)):
        shifts.append(get_shift_right(string, i))
    if not shifts:
        shifts = ["", ]
    return shifts


def sort_values(strings):
    return sorted(strings)


def get_original_index(string: str, strings: list):
    return strings.index(string)


def get_last_column(strings):
    try:
        last_column = "".join(list(zip(*strings))[-1])
    except IndexError:
        last_column = ""
    return last_column


def encode(s):
    strings = get_all_shifts(s)
    sorted_strings = sort_values(strings)
    index = get_original_index(s, sorted_strings)
    last_column = get_last_column(sorted_strings)
    return last_column, index


def decode(s, n):
    strings = sort_values(list(s))
    for iter in range(1, len(s)):
        for num, char in enumerate(s):
            strings[num] = char + strings[num]
        strings = sort_values(strings)
    try:
        result = strings[n]
    except IndexError:
        result = ""
    return result


class TestStringMethods(unittest.TestCase):
    def test_shift_right(self):
        self.assertEqual(get_shift_right("bananabar", 1), "rbananaba")

    def test_all_shifts(self):
        self.assertEqual(get_all_shifts("bananabar"), [
                "bananabar",
                "rbananaba",
                "arbananab",
                "barbanana",
                "abarbanan",
                "nabarbana",
                "anabarban",
                "nanabarba",
                "ananabarb",
            ])

    def test_sort_strings(self):
        self.assertListEqual(sort_values([
            "bananabar",
            "rbananaba",
            "arbananab",
            "barbanana",
            "abarbanan",
            "nabarbana",
            "anabarban",
            "nanabarba",
            "ananabarb",
        ]), [
            "abarbanan",
            "anabarban",
            "ananabarb",
            "arbananab",
            "bananabar",
            "barbanana",
            "nabarbana",
            "nanabarba",
            "rbananaba",
        ])

    def test_get_index(self):
        self.assertEqual(get_original_index("bananabar", [
            "abarbanan",
            "anabarban",
            "ananabarb",
            "arbananab",
            "bananabar",
            "barbanana",
            "nabarbana",
            "nanabarba",
            "rbananaba",
        ]), 4)

    def test_last_column(self):
        self.assertEqual(get_last_column([
            "abarbanan",
            "anabarban",
            "ananabarb",
            "arbananab",
            "bananabar",
            "barbanana",
            "nabarbana",
            "nanabarba",
            "rbananaba",
        ]), "nnbbraaaa")

    def test_encode1(self):
        self.assertEqual(encode("bananabar"), ("nnbbraaaa", 4))

    def test_encode2(self):
        self.assertEqual(encode("Humble Bundle"), ("e emnllbduuHB", 2))

    def test_encode3(self):
        self.assertEqual(encode("Mellow Yellow"), ("ww MYeelllloo", 1))

    def test_encode4(self):
        self.assertEqual(encode("a"), ("a", 0))

    def test_encode5(self):
        self.assertEqual(encode(""), ("", 0))

    def test_decode1(self):
        self.assertEqual(decode("nnbbraaaa", 4), "bananabar")

    def test_decode2(self):
        self.assertEqual(decode("e emnllbduuHB", 2), "Humble Bundle")

    def test_decode3(self):
        self.assertEqual(decode("ww MYeelllloo", 1), "Mellow Yellow")

    def test_decode4(self):
        self.assertEqual(decode("", 0), "")


if __name__ == '__main__':
    unittest.main()
