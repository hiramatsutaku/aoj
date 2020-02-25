import unittest
import main


class TestMain(unittest.TestCase):
    def test_judge(self):
        self.assertEqual('Yes', main.judge(0, 1, 2))
        self.assertEqual('No', main.judge(0, 0, 0))
        self.assertEqual('No', main.judge(0, 1, 1))
        self.assertEqual('No', main.judge(2, 1, 1))
