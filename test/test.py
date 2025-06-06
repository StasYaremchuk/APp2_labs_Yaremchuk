import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from pair_counter import count_elements, build_groups, in_group, count_pairs

class TestPairCounter(unittest.TestCase):

    def test_count_elements(self):
        self.assertEqual(count_elements([]), 0)
        self.assertEqual(count_elements([1, 2, 3]), 3)
        self.assertEqual(count_elements("abc"), 3)

    def test_build_groups(self):
        edges = [(1, 2), (3, 4)]
        expected = [[1, 2], [3, 4]]
        self.assertEqual(build_groups(edges), expected)

    def test_in_group(self):
        group = [1, 2, 3]
        self.assertTrue(in_group(group, 2))
        self.assertFalse(in_group(group, 5))

    def test_count_pairs_simple(self):
        groups = [[1, 2], [3, 4]]
        self.assertEqual(count_pairs(groups), 2)

    def test_count_pairs_complex(self):
        groups = [[1, 2, 3], [4, 6], [5]]
        self.assertEqual(count_pairs(groups), 7)

    def test_count_pairs_no_pairs(self):
        groups = [[2, 4], [6, 8]]
        self.assertEqual(count_pairs(groups), 0)

if __name__ == '__main__':
    unittest.main()
