import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual('1 17 37', main.calc(5, [10, 1, 5, 4, 17]))
