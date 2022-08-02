import unittest
from get_second_max import get_second_max


class Get_second_max(unittest.TestCase):
    def test_second_max(self):
        self.assertEqual(get_second_max([1, 2, 3, 4, 5]), 4)
        self.assertEqual(get_second_max([1, 2, 3, 4, 4, 5]), 4)
        self.assertEqual(get_second_max([1, 2, 3, 4, 4, 5, 6, 9, 9, 7]), 9)
        self.assertEqual(get_second_max([]), 0)
        self.assertEqual(get_second_max([1]), 0)
        self.assertEqual(get_second_max([1, 2]), 1)
        self.assertEqual(get_second_max([2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
