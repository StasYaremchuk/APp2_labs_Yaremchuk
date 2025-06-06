import unittest
import sys
import os

sys.path.append(os.path.abspath('../src'))
from lab4 import ProductQueue  

class TestProductQueue(unittest.TestCase):

    def setUp(self):
        self.pq = ProductQueue()
        self.pq.insert("A1", "Хліб", 10)
        self.pq.insert("B2", "Молоко", 25)
        self.pq.insert("C3", "Сік", 8)
        self.pq.insert("D4", "Яблука", 15)
        self.pq.insert("E5", "Печиво", 30)

    def test_insert_duplicate(self):
        self.pq.insert("A1", "Ковбаса", 20)
        items = self.pq.display()
        self.assertEqual(len(items), 5)  # Кількість товарів не має змінитись

    def test_display_order(self):
        result = self.pq.display()
        sales_list = [item[2] for item in result]
        self.assertEqual(sales_list, sorted(sales_list))

    def test_peek(self):
        top = self.pq.peek()
        self.assertIsNotNone(top)
        self.assertEqual(top.product_id, "E5")
        self.assertEqual(top.sales, 30)

    def test_del_max(self):
        removed = self.pq.del_max()
        self.assertEqual(removed.product_id, "E5")
        self.assertEqual(removed.name, "Печиво")
        top_after = self.pq.peek()
        self.assertEqual(top_after.product_id, "B2")  # Молоко має стати найпопулярнішим

    def test_del_max_on_empty(self):
        empty_q = ProductQueue()
        removed = empty_q.del_max()
        self.assertIsNone(removed)

    def test_peek_on_empty(self):
        empty_q = ProductQueue()
        self.assertIsNone(empty_q.peek())


if __name__ == '__main__':
    unittest.main()
