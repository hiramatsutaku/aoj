import unittest
import main


class TestMain(unittest.TestCase):
    def test_format(self):
        self.assertEqual('0:0:0', main.format(0))
        self.assertEqual('0:0:1', main.format(1))
        self.assertEqual('0:0:59', main.format(59))
        self.assertEqual('0:1:0', main.format(60))
        self.assertEqual('1:0:0', main.format(3600))
        self.assertEqual('1:0:1', main.format(3601))
        self.assertEqual('1:1:1', main.format(3661))
