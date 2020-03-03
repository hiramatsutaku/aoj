import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            'Fair, later, occasionally cloudy.',
            main.main('fAIR, LATER, OCCASIONALLY CLOUDY.')
        )
