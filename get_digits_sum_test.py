import unittest
from get_digits_sum import get_digits_sum


class GetDegreeTest(unittest.TestCase):
    def testCheckSum(self):
        self.assertEqual(get_digits_sum(1), 1)
        self.assertEqual(get_digits_sum(12), 3)
        self.assertEqual(get_digits_sum(123), 6)
        self.assertEqual(get_digits_sum(0), 0)


if __name__ == "__main__":
    unittest.main()
