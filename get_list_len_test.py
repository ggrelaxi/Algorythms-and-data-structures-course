import unittest
from get_list_len import get_list_len


class Get_list_len(unittest.TestCase):
    def test_get_list_len(self):
        self.assertEqual(get_list_len([]), 0)
        self.assertEqual(get_list_len([1]), 1)
        self.assertEqual(get_list_len([1, 2, 3]), 3)
        self.assertEqual(get_list_len([1, 2, 3, 4, 5]), 5)


if __name__ == "__main__":
    unittest.main()
