import unittest

from katas.word_count import word_count


class TestWordCount(unittest.TestCase):
    def test_counts_words_separated_by_single_spaces(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_counts_a_single_word(self):
        self.assertEqual(word_count("hello"), 1)

    def test_empty_string_has_no_words(self):
        self.assertEqual(word_count(""), 0)

    def test_whitespace_only_has_no_words(self):
        self.assertEqual(word_count("   \t\n"), 0)

    def test_repeated_whitespace_is_one_separator(self):
        self.assertEqual(word_count("  one   two\tthree\nfour  "), 4)

    def test_punctuation_stays_attached_to_its_word(self):
        self.assertEqual(word_count("hello, world!"), 2)
