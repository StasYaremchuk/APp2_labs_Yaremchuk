import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))

from lab3 import BinaryTree, invert_binary_tree


def level_order_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.value)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        queue = next_queue
    return result


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        self.assertEqual(level_order_list(root), [
            [1],
            [2, 3],
            [4, 5, 6, 7]
        ])

        invert_binary_tree(root)

        self.assertEqual(level_order_list(root), [
            [1],
            [3, 2],
            [7, 6, 5, 4]
        ])

    def test_single_node(self):
        root = BinaryTree(42)
        self.assertEqual(level_order_list(root), [[42]])
        invert_binary_tree(root)
        self.assertEqual(level_order_list(root), [[42]])

    def test_none(self):
        self.assertIsNone(invert_binary_tree(None))

unittest.main()
