import unittest
from get_degree import get_degree


class GetDegreeTest(unittest.TestCase):
    def testGetDegree(self):
        self.assertEqual(get_degree(2, 2), 4)
        self.assertEqual(get_degree(2, 3), 8)
        self.assertEqual(get_degree(2, 10), 1024)


if __name__ == "__main__":
    unittest.main()
