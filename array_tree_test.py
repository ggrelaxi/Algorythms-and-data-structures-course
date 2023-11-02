import unittest
from array_tree import aBST


class ABSTTest(unittest.TestCase):
    def testSize(self):
        self.assertEqual(len(aBST(0).Tree), 1)
        self.assertEqual(len(aBST(1).Tree), 3)
        self.assertEqual(len(aBST(2).Tree), 7)

    def testAddKeyRoot(self):
        atree = aBST(2)

        self.assertEqual(atree.AddKey(1), 0)
        self.assertEqual(atree.Tree[0], 1)

    def testfAddKeyLeftChild(self):
        atree = aBST(2)

        atree.AddKey(7)
        atree.AddKey(4)
        atree.AddKey(10)

        self.assertEqual(atree.Tree[1], 4)

        atree.AddKey(8)

        self.assertEqual(atree.Tree[5], 8)

    def testAddRightChild(self):
        atree = aBST(2)

        atree.AddKey(5)
        atree.AddKey(3)
        atree.AddKey(6)

        self.assertEqual(atree.Tree[2], 6)

        atree.AddKey(4)

        self.assertEqual(atree.Tree[4], 4)

    def testAddKeyFromFullTree(self):
        atree = aBST(1)

        atree.AddKey(5)
        atree.AddKey(3)
        atree.AddKey(6)

        self.assertEqual(atree.AddKey(4), -1)

    def testFindAtEmptyTree(self):
        atree = aBST(0)

        self.assertEqual(atree.FindKeyIndex(5), -1)

    def testFindSingleItemInTree(self):
        atree = aBST(0)
        atree.AddKey(5)

        self.assertEqual(atree.FindKeyIndex(5), 0)

    def findItemInDepth(self):
        atree = aBST(1)
        atree.AddKey(5)
        atree.AddKey(3)
        atree.AddKey(6)

        self.assertEqual(atree.FindKeyIndex(5), 0)
        self.assertEqual(atree.FindKeyIndex(3), 1)
        self.assertEqual(atree.FindKeyIndex(6), 2)

    def findItemInDepthWithoutTargetKey(self):
        atree = aBST(1)
        atree.AddKey(5)
        self.assertEqual(atree.FindKeyIndex(3), None)
        self.assertEqual(atree.FindKeyIndex(6), None)
        atree.AddKey(3)
        atree.AddKey(6)
        self.assertEqual(atree.FindKeyIndex(3), -1)
        self.assertEqual(atree.FindKeyIndex(6), -1)


if __name__ == "__main__":
    unittest.main()
