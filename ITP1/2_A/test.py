import unittest
import main


class TestMain(unittest.TestCase):
    def test_convert(self):
        self.assertEqual('a == b', main.convert(-1000, -1000))
        self.assertEqual('a < b', main.convert(-1000, 1000))
        self.assertEqual('a > b', main.convert(1000, -1000))
        self.assertEqual('a == b', main.convert(0, 0))
