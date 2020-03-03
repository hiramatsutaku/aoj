import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            main.main(6, [5, 2, 4, 6, 1, 3])
        )
