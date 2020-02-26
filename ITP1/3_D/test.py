import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(2, main.count_divisor(1, 2, 1000))
        self.assertEqual(2, main.count_divisor(1, 3, 1000))
        self.assertEqual(3, main.count_divisor(1, 4, 1000))
