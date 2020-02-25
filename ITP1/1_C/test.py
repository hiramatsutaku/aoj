import unittest
import main


class TestMain(unittest.TestCase):
    def test_calc_area(self):
        self.assertEqual(1, main.calc_area(1, 1))
        self.assertEqual(10000, main.calc_area(100, 100))
        self.assertEqual(20, main.calc_area(2, 10))

    def test_calc_surrounding_length(self):
        self.assertEqual(4, main.calc_surrounding_length(1, 1))
        self.assertEqual(400, main.calc_surrounding_length(100, 100))
        self.assertEqual(24, main.calc_surrounding_length(2, 10))
