import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from lab8 import ford_fulkerson

class TestFordFulkerson(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_roads.csv"
        content = (
            "F1,F2,F3\n"
            "S1,S2,S3,S4,S5\n"
            "F1,X1,5\n"
            "F2,X2,7\n"
            "F3,X3,6\n"
            "X1,X2,3\n"
            "X2,X3,4\n"
            "X1,S1,4\n"
            "X2,S2,5\n"
            "X3,S3,7\n"
            "X3,S4,3\n"
            "X2,S5,2\n"
        )
        with open(self.test_file, "w") as f:
            f.write(content)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_max_flow(self):
        result = ford_fulkerson(self.test_file)
        self.assertEqual(result, 18)

if __name__ == "__main__":
    unittest.main()
