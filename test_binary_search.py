import unittest

from BinarySearch import (
    binary_search_any,
    binary_search_first,
    binary_search_last,
    binary_search_range,
)


class TestBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(binary_search_any([], 5))
        self.assertIsNone(binary_search_first([], 5))
        self.assertIsNone(binary_search_last([], 5))
        self.assertEqual(binary_search_range([], 5), (None, None))

    def test_single_item_found(self):
        self.assertEqual(binary_search_any([7], 7), 0)
        self.assertEqual(binary_search_first([7], 7), 0)
        self.assertEqual(binary_search_last([7], 7), 0)
        self.assertEqual(binary_search_range([7], 7), (0, 0))

    def test_single_item_not_found(self):
        self.assertIsNone(binary_search_any([7], 3))
        self.assertIsNone(binary_search_first([7], 3))
        self.assertIsNone(binary_search_last([7], 3))
        self.assertEqual(binary_search_range([7], 3), (None, None))

    def test_multiple_distinct_values(self):
        numbers = [1, 2, 4, 6, 8, 9]
        self.assertIn(binary_search_any(numbers, 4), [2])
        self.assertEqual(binary_search_first(numbers, 4), 2)
        self.assertEqual(binary_search_last(numbers, 4), 2)
        self.assertEqual(binary_search_range(numbers, 4), (2, 2))

    def test_multiple_duplicates(self):
        numbers = [1, 2, 2, 2, 3, 3, 5]
        self.assertIn(binary_search_any(numbers, 2), [1, 2, 3])
        self.assertEqual(binary_search_first(numbers, 2), 1)
        self.assertEqual(binary_search_last(numbers, 2), 3)
        self.assertEqual(binary_search_range(numbers, 2), (1, 3))

    def test_all_duplicates(self):
        numbers = [4, 4, 4, 4]
        self.assertIn(binary_search_any(numbers, 4), [0, 1, 2, 3])
        self.assertEqual(binary_search_first(numbers, 4), 0)
        self.assertEqual(binary_search_last(numbers, 4), 3)
        self.assertEqual(binary_search_range(numbers, 4), (0, 3))

    def test_target_before_first(self):
        numbers = [10, 20, 30]
        self.assertIsNone(binary_search_any(numbers, 5))
        self.assertIsNone(binary_search_first(numbers, 5))
        self.assertIsNone(binary_search_last(numbers, 5))
        self.assertEqual(binary_search_range(numbers, 5), (None, None))

    def test_target_after_last(self):
        numbers = [10, 20, 30]
        self.assertIsNone(binary_search_any(numbers, 40))
        self.assertIsNone(binary_search_first(numbers, 40))
        self.assertIsNone(binary_search_last(numbers, 40))
        self.assertEqual(binary_search_range(numbers, 40), (None, None))

    def test_negative_values(self):
        numbers = [-5, -3, -3, -1, 0, 2]
        self.assertEqual(binary_search_first(numbers, -3), 1)
        self.assertEqual(binary_search_last(numbers, -3), 2)
        self.assertEqual(binary_search_range(numbers, -3), (1, 2))

    def test_large_range(self):
        numbers = list(range(0, 100, 2))
        self.assertEqual(binary_search_any(numbers, 20), 10)
        self.assertEqual(binary_search_first(numbers, 20), 10)
        self.assertEqual(binary_search_last(numbers, 20), 10)
        self.assertEqual(binary_search_range(numbers, 20), (10, 10))


if __name__ == "__main__":
    unittest.main()
