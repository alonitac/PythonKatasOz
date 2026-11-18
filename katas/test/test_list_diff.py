import unittest

from katas.list_diff import list_diff


class TestListDiff(unittest.TestCase):
    def test_first_item_is_none_and_each_later_item_is_minus_the_previous(self):
        self.assertEqual(list_diff([10, 7, 12]), [None, -3, 5])

    def test_equal_neighbors_differ_by_zero(self):
        self.assertEqual(list_diff([5, 5, 8]), [None, 0, 3])

    def test_rising_sequence(self):
        self.assertEqual(list_diff([1, 3, 6, 10]), [None, 2, 3, 4])

    def test_single_element_is_only_none(self):
        self.assertEqual(list_diff([4]), [None])

    def test_empty_list_stays_empty(self):
        self.assertEqual(list_diff([]), [])
