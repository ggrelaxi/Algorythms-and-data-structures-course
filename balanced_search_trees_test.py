import unittest
from balanced_search_trees import GenerateBBSTArray


class GenerateBBSTArrayTest(unittest.TestCase):
    def testCreateBBstDepth1(self):
        a = [1, 5, 3]
        bbst = GenerateBBSTArray(a)

        self.assertEqual(bbst, [3, 1, 5])

    def testCreateBBstDepth2(self):
        a = [1, 7, 6, 5, 3, 4, 8]
        bbst = GenerateBBSTArray(a)

        self.assertEqual(bbst, [5, 3, 7, 1, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
