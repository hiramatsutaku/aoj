import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            '1 8 5\n0 9 6\n4 23 14',
            main.main(
                3, 2, 3,
                [[1, 2], [0, 3], [4, 5]],
                [[1, 2, 1], [0, 3, 2]],
            )
        )
