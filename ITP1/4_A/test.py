import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual('1 1 1.50000', main.calc(3, 2))
        self.assertEqual('2 0 2', main.calc(4, 2))
