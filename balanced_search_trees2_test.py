import unittest
from balanced_search_trees2 import BalancedBST, BSTNode


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

    def testUnbalancedDeepLeftTree(self):
        root = BSTNode(3, None)
        l_lvl1 = BSTNode(2, root)
        root.LeftChild = l_lvl1
        l_lvl2 = BSTNode(1, l_lvl1)
        l_lvl1.LeftChild = l_lvl2

        tree = BalancedBST()
        
        self.assertEqual(tree.IsBalanced(root), False)

    def testUnbalancedDeepRightTree(self):
        root = BSTNode(1, None)
        r_lvl1 = BSTNode(2, root)
        root.RightChild  = r_lvl1
        r_lvl2 = BSTNode(3, r_lvl1)
        r_lvl1.RightChild = r_lvl2

        tree = BalancedBST()

        self.assertEqual(tree.IsBalanced(root), False)
    
    def testInvalidKeysOrderLeft(self):
        root = BSTNode(5, None)
        r_lvl1 = BSTNode(6, root)
        root.LeftChild = r_lvl1
        

        tree = BalancedBST()

        self.assertEqual(tree.IsBalanced(root), False)

    def testInvalidKeysOrderRight(self):
        root = BSTNode(6, None)
        r_lvl1 = BSTNode(5, root)
        root.RightChild = r_lvl1
        

        tree = BalancedBST()

        self.assertEqual(tree.IsBalanced(root), False)

if __name__ == "__main__":
    unittest.main()