import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from lab9 import counting_sort, get_max

class TestWordChain(unittest.TestCase):

    def setUp(self):
        self.input_file = "wchain.in"
        self.output_file = "wchain.out"

    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def write_input(self, lines):
        with open(self.input_file, "w") as f:
            f.write("\n".join(lines) + "\n")

    def read_output(self):
        with open(self.output_file) as f:
            return f.read().strip()

    def test_case_1(self):
        data = [
            "5",
            "a",
            "b",
            "ba",
            "bca",
            "bdca"
        ]
        self.write_input(data)
        import wchain
        self.assertEqual(self.read_output(), "4")

    def test_case_2(self):
        data = [
            "6",
            "a",
            "ab",
            "abc",
            "abcd",
            "x",
            "xyz"
        ]
        self.write_input(data)
        import wchain
        self.assertEqual(self.read_output(), "4")

    def test_case_3(self):
        data = [
            "3",
            "x",
            "xy",
            "yx"
        ]
        self.write_input(data)
        import wchain
        self.assertEqual(self.read_output(), "2")

    def test_empty_input(self):
        data = [
            "0"
        ]
        self.write_input(data)
        import wchain
        self.assertEqual(self.read_output(), "0")

    def test_counting_sort(self):
        words = ["apple", "a", "app", "ap"]
        sorted_words = counting_sort(words)
        self.assertEqual(sorted_words, ["a", "ap", "app", "apple"])

    def test_get_max(self):
        values = [1, 3, 2, 5, 4]
        self.assertEqual(get_max(values), 5)

if __name__ == "__main__":
    unittest.main()
