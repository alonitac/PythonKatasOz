import unittest

from katas.is_unique_str import is_unique_str


class TestIsUniqueStr(unittest.TestCase):
    def test_all_different_characters_are_unique(self):
        self.assertTrue(is_unique_str("abc"))

    def test_a_repeated_character_is_not_unique(self):
        self.assertFalse(is_unique_str("aab"))

    def test_empty_string_is_unique(self):
        self.assertTrue(is_unique_str(""))

    def test_single_character_is_unique(self):
        self.assertTrue(is_unique_str("a"))

    def test_uppercase_and_lowercase_count_as_different(self):
        self.assertTrue(is_unique_str("Aa"))

    def test_a_repeated_space_is_not_unique(self):
        self.assertFalse(is_unique_str("a a"))
