import unittest

from katas.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_returns_the_shorter_string_when_it_is_a_prefix(self):
        self.assertEqual(longest_common_prefix("flow", "flower"), "flow")

    def test_returns_the_shared_start(self):
        self.assertEqual(longest_common_prefix("interspecies", "interstellar"), "inters")

    def test_returns_empty_when_nothing_is_shared(self):
        self.assertEqual(longest_common_prefix("dog", "cat"), "")

    def test_identical_strings_return_the_whole_string(self):
        self.assertEqual(longest_common_prefix("abc", "abc"), "abc")

    def test_an_empty_argument_has_no_prefix(self):
        self.assertEqual(longest_common_prefix("", "abc"), "")
        self.assertEqual(longest_common_prefix("abc", ""), "")

    def test_comparison_is_case_sensitive(self):
        self.assertEqual(longest_common_prefix("Abc", "abc"), "")
