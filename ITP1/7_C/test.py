import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            '1 2 0 3\n0 3 0 3\n1 5 0 6',
            main.main(2, 3, [[1, 2, 0], [0, 3, 0]])
        )
