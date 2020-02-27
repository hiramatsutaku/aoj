import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual('5\n6\n9\n', main.main(
            [
                [1, 2, 0, 1],
                [0, 3, 0, 1],
                [4, 1, 1, 0],
            ],
            [1, 2, 3, 0])
        )
