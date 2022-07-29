import unittest
from get_degree import get_degree


class GetDegreeTest(unittest.TestCase):
    def testGetDegree(self):
        self.assertEqual(get_degree(2, 2), 4)
        self.assertEqual(get_degree(2, 3), 8)
        self.assertEqual(get_degree(2, 10), 1024)
        self.assertEqual(get_degree(10, 0), 1)
        self.assertEqual(get_degree(2, 0), 1)

    def testGetBaseZeroDegree(self):
        self.assertEqual(get_degree(0, 1), 0)
        self.assertEqual(get_degree(0, 10), 0)
        self.assertEqual(get_degree(0, 0), 1)
    
    def testNegativeBaseDegree(self):
        self.assertEqual(get_degree(-2, 2), 4)
        self.assertEqual(get_degree(-2, 3), -8)

    


if __name__ == "__main__":
    unittest.main()
