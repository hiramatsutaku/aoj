import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            [
                'a : 1',
                'b : 0',
                'c : 0',
                'd : 0',
                'e : 1',
                'f : 0',
                'g : 0',
                'h : 1',
                'i : 2',
                'j : 0',
                'k : 0',
                'l : 0',
                'm : 0',
                'n : 1',
                'o : 0',
                'p : 1',
                'q : 0',
                'r : 0',
                's : 2',
                't : 1',
                'u : 0',
                'v : 0',
                'w : 0',
                'x : 0',
                'y : 0',
                'z : 0'
            ],
            main.main('This is a pen.')
        )
