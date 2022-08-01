import unittest
from check_palindrome_str import check_palindrome_str


class Check_palindrom_str(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(check_palindrome_str('aba'), True)
        self.assertEqual(check_palindrome_str('ab'), False)
        self.assertEqual(check_palindrome_str('a'), True)
        self.assertEqual(check_palindrome_str('ababa'), True)
        self.assertEqual(check_palindrome_str('abvda'), False)


if __name__ == "__main__":
    unittest.main()
