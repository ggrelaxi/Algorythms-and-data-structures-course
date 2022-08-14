import unittest
from binary_trees import BST, BSTNode


class BSTTest(unittest.TestCase):
    def testAddKeyValue(self):
        root = BSTNode(8, 'rootKey', None)
        tree = BST(root)

        self.assertEqual(tree.Root, root)
        tree.AddKeyValue(4, 'n1_left')
        tree.AddKeyValue(12, 'n1_right')

        four_search_result = tree.FindNodeByKey(4)
        twelwe_search_result = tree.FindNodeByKey(12)

        self.assertEqual(four_search_result.Node.NodeKey, 4)
        self.assertEqual(twelwe_search_result.Node.NodeKey, 12)

    def testFindNodeByKey(self):
        root = BSTNode(8, 'rootKey', None)
        tree = BST(None)

        empty_find_result = tree.FindNodeByKey(8)

        self.assertEqual(empty_find_result.Node, None)
        self.assertEqual(empty_find_result.NodeHasKey, False)
        self.assertEqual(empty_find_result.ToLeft, False)

        tree.Root = root

        root_node_find_result = tree.FindNodeByKey(8)

        self.assertEqual(root_node_find_result.Node, root)
        self.assertEqual(root_node_find_result.NodeHasKey, True)
        self.assertEqual(root_node_find_result.ToLeft, False)

    def testMinMax(self):
        root = BSTNode(8, 'rootKey', None)
        tree = BST(root)

        self.assertEqual(tree.Root, root)
        tree.AddKeyValue(4, 'n1_left')
        tree.AddKeyValue(12, 'n1_right')

        self.assertEqual(tree.FinMinMax(tree.Root, True), 12)
        self.assertEqual(tree.FinMinMax(tree.Root, False), 4)
        self.assertEqual(tree.FinMinMax(root.LeftChild, True), 4)
        self.assertEqual(tree.FinMinMax(root.RightChild, False), 12)

    def testCount(self):
        root = BSTNode(8, 'rootKey', None)
        tree = BST(None)

        self.assertEqual(tree.Count(), 0)

        tree.Root = root

        self.assertEqual(tree.Count(), 1)

        tree.AddKeyValue(4, 'n1_left')

        self.assertEqual(tree.Count(), 2)

        tree.AddKeyValue(12, 'n1_right')

        self.assertEqual(tree.Count(), 3)

    def testDelete(self):
        root = BSTNode(8, 'rootKey', None)
        tree = BST(root)

        tree.DeleteNodeByKey(8)

        self.assertEqual(tree.Root, None)

        tree.Root = root

        tree.AddKeyValue(4, 'n1_left')
        tree.AddKeyValue(12, 'n1_right')

        tree.DeleteNodeByKey(4)

        self.assertEqual(tree.FindNodeByKey(4).Node, root)

        tree.DeleteNodeByKey(12)

        self.assertEqual(tree.FindNodeByKey(12).Node, root)

        root1 = BSTNode(8, 'rootKey', None)
        tree1 = BST(root1)
        tree1.AddKeyValue(4, 'n1_left')
        tree1.AddKeyValue(12, 'n1_right')
        tree1.AddKeyValue(10, 'n2_left')
        tree1.AddKeyValue(14, 'n2_right')
        tree1.AddKeyValue(15, 'n3_right')

        tree1.DeleteNodeByKey(10)

        self.assertEqual(tree1.FindNodeByKey(10).Node.NodeKey, 12)

        root2 = BSTNode(8, 'rootKey', None)
        tree2 = BST(root2)
        tree2.AddKeyValue(4, 'n1_left')
        tree2.AddKeyValue(12, 'n1_right')
        tree2.AddKeyValue(10, 'n2_left')
        tree2.AddKeyValue(14, 'n2_right')
        tree2.AddKeyValue(15, 'n3_right')

        tree2.DeleteNodeByKey(14)

        self.assertEqual(tree2.FindNodeByKey(12).Node.RightChild.NodeKey, 15)

        root3 = BSTNode(8, 'rootKey', None)
        tree3 = BST(root3)
        tree3.AddKeyValue(4, 'n1_left')
        tree3.AddKeyValue(12, 'n1_right')
        tree3.AddKeyValue(10, 'n2_left')
        tree3.AddKeyValue(14, 'n2_right')
        tree3.AddKeyValue(13, 'n3_left')
        tree3.AddKeyValue(15, 'n3_right')

        tree3.DeleteNodeByKey(12)

        self.assertEqual(tree3.FindNodeByKey(13).Node.RightChild.NodeKey, 14)
        self.assertEqual(tree3.FindNodeByKey(13).Node.LeftChild.NodeKey, 10)
        self.assertEqual(tree3.Root.RightChild.NodeKey, 13)


if __name__ == "__main__":
    unittest.main()
