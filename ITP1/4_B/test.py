import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual('12.566371 12.566371', main.calc(2))
        self.assertEqual('28.274334 18.849556', main.calc(3))
