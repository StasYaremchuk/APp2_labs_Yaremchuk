import unittest
import os
import sys

sys.path.append(os.path.abspath('../src'))
from lab5 import build_tree_from_input, min_depth


class TestTreeFunctions(unittest.TestCase):

    def setUp(self):
        self.test_file = "tests/test_input.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def write_file(self, content):
        with open(self.test_file, 'w') as f:
            f.write(content)

    def test_single_node(self):
        self.write_file("1\n")
        root = build_tree_from_input(self.test_file)
        self.assertEqual(min_depth(root), 1)

    def test_full_binary_tree_depth_3(self):
        self.write_file("1\n2 3\n4 5 6 7\n")
        root = build_tree_from_input(self.test_file)
        self.assertEqual(min_depth(root), 3)

    def test_tree_with_missing_children(self):
        self.write_file("1\n2 None\nNone None\n")
        root = build_tree_from_input(self.test_file)
        self.assertEqual(min_depth(root), 2)

    def test_empty_tree(self):
        self.write_file("")
        root = build_tree_from_input(self.test_file)
        self.assertEqual(min_depth(root), 0)

    def test_left_skewed_tree(self):
        self.write_file("1\n2 None\n3 None\n4 None\n")
        root = build_tree_from_input(self.test_file)
        self.assertEqual(min_depth(root), 4)


if __name__ == '__main__':
    unittest.main()
