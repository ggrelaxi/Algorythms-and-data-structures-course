import unittest
from balanced_search_trees2 import BalancedBST


class GenerateBBSTTest(unittest.TestCase):
    def testEmptyTree(self):
        a = []

        tree = BalancedBST()
        tree.GenerateTree(a)

        self.assertEqual(tree.Root, None)

    def testSingleNode(self):
        a = [1]

        tree = BalancedBST()
        tree.GenerateTree(a)
        root = tree.Root

        self.assertEqual(root.Parent, None)
        self.assertEqual(root.NodeKey, 1)
        self.assertEqual(root.LeftChild, None)
        self.assertEqual(root.RightChild, None)
        self.assertEqual(root.Level, 0)

    def testTreeWithChild(self):
        a = [4,2,3] # [2,3,4]

        tree = BalancedBST()
        tree.GenerateTree(a)
        root = tree.Root

        self.assertEqual(root.LeftChild.Parent, root)
        self.assertEqual(root.RightChild.Parent, root)
        self.assertEqual(root.LeftChild.NodeKey, 2)
        self.assertEqual(root.RightChild.NodeKey, 4)
        self.assertEqual(root.LeftChild.Level, 1)
        self.assertEqual(root.RightChild.Level, 1)
        self.assertEqual(root.LeftChild.LeftChild, None)
        self.assertEqual(root.LeftChild.RightChild, None)
        self.assertEqual(root.RightChild.LeftChild, None)
        self.assertEqual(root.RightChild.RightChild, None)

    def testIsBalancedEmptyTree(self):
        a = []
        
        tree = BalancedBST()
        tree.GenerateTree(a)
        
        self.assertEqual(tree.IsBalanced(tree.Root), True)

    def testIsBalancedSingleNodeTree(self):
        a = [1]
        
        tree = BalancedBST()
        tree.GenerateTree(a)

        self.assertEqual(tree.IsBalanced(tree.Root), True)
    
    def testIsBalancedDeepTree(self):
        a = [1,2,3]

        tree = BalancedBST()
        tree.GenerateTree(a)

        self.assertEqual(tree.IsBalanced(tree.Root), True)

    def testUnbalancedDeepTree(self):
        a = [1,1,2,3,3,3,3]

        tree = BalancedBST()
        tree.GenerateTree(a)

        self.assertEqual(tree.IsBalanced(tree.Root), False)

    def testUnbalancedDeepLeftTree(self):
        a = [1,1,1,1,1,2,3]

        tree = BalancedBST()
        tree.GenerateTree(a)
        self.assertEqual(tree.IsBalanced(tree.Root), False) 

if __name__ == "__main__":
    unittest.main()