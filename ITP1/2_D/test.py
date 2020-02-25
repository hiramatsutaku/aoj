import unittest
import main


class TestMain(unittest.TestCase):
    def test_judge(self):
        self.assertEqual('Yes', main.is_in(10, 10, 2, 2, 1))
        self.assertEqual('No', main.is_in(2, 2, 2, 2, 1))
