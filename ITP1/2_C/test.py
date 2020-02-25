import unittest
import main


class TestMain(unittest.TestCase):
    def test_judge(self):
        self.assertEqual('1 1 1', main.sort(1, 1, 1))
        self.assertEqual('1 1 2', main.sort(1, 1, 2))
        self.assertEqual('1 2 3', main.sort(3, 2, 1))
        self.assertEqual('1 1 2', main.sort(2, 1, 1))
        self.assertEqual('1 2 2', main.sort(2, 2, 1))
        self.assertEqual('1 1 2', main.sort(1, 2, 1))
