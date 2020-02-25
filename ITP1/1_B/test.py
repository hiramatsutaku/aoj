import unittest
import main


class TestMain(unittest.TestCase):
    def test_calc_cubed(self):
        self.assertEqual(8, main.calc_cubed(2))
        self.assertEqual(27, main.calc_cubed(3))
        self.assertEqual(64, main.calc_cubed(4))
