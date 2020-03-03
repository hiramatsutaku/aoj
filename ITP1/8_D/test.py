import unittest
import main


class TestMain(unittest.TestCase):
    def test_count_divisor(self):
        self.assertEqual(
            'Yes',
            main.main('vanceknowledgetoad', 'advance')
        )
        self.assertEqual(
            'No',
            main.main('vanceknowledgetoad', 'advanced')
        )
