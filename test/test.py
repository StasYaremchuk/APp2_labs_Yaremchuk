import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from lab7 import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):

    def test_single_match(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(boyer_moore_search(haystack, needle), [6])

    def test_multiple_matches(self):
        haystack = "abcabcabc"
        needle = "abc"
        self.assertEqual(boyer_moore_search(haystack, needle), [0, 3, 6])

    def test_no_match(self):
        haystack = "abcdef"
        needle = "xyz"
        self.assertEqual(boyer_moore_search(haystack, needle), [])

    def test_empty_needle(self):
        haystack = "abc"
        needle = ""
        self.assertEqual(boyer_moore_search(haystack, needle), [])

    def test_needle_longer_than_haystack(self):
        haystack = "abc"
        needle = "abcdef"
        self.assertEqual(boyer_moore_search(haystack, needle), [])

    def test_full_match(self):
        haystack = "match"
        needle = "match"
        self.assertEqual(boyer_moore_search(haystack, needle), [0])

    def test_overlap(self):
        haystack = "aaaaa"
        needle = "aa"
        self.assertEqual(boyer_moore_search(haystack, needle), [0, 2])

if __name__ == '__main__':
    unittest.main()
