import unittest
from binary_trees import BSTNode, BSTFind, BST


class BSTTest(unittest.TestCase):
    def testFindEmptyTree(self):
        tree = BST(None)

        self.assertEqual(tree.FindNodeByKey(1).Node, None)

    def testCount(self):
        tree = BST(None)

        self.assertEqual(tree.Count(), 0)

        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.Count(), 1)

    def testAddRootNode(self):
        tree = BST(None)
        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.Root.NodeKey, 1)
        self.assertEqual(tree.Root.NodeValue, 1)
        self.assertEqual(tree.Count(), 1)

    def testAddLeftChild(self):
        tree = BST(None)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.Count(), 2)
        findResult = tree.FindNodeByKey(1)

        self.assertEqual(findResult.Node.NodeKey, 1)
        self.assertEqual(findResult.Node.NodeValue, 1)
        self.assertEqual(findResult.Node.Parent, tree.Root)

    def testAddRightChild(self):
        tree = BST(None)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(3, 3)

        self.assertEqual(tree.Count(), 2)
        findResult = tree.FindNodeByKey(3)

        self.assertEqual(findResult.Node.NodeKey, 3)
        self.assertEqual(findResult.Node.NodeValue, 3)
        self.assertEqual(findResult.Node.Parent, tree.Root)

    def testAddToLeftTarget(self):
        tree = BST(None)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)

        findResult = tree.FindNodeByKey(2)

        self.assertEqual(findResult.Node.NodeKey, 3)
        self.assertEqual(findResult.Node.NodeValue, 3)
        self.assertEqual(findResult.Node.Parent, tree.Root)
        self.assertEqual(findResult.NodeHasKey, False)
        self.assertEqual(findResult.ToLeft, True)

    def testAddToRightTarget(self):
        tree = BST(None)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)

        findResult = tree.FindNodeByKey(6)

        self.assertEqual(findResult.Node.NodeKey, 5)
        self.assertEqual(findResult.Node.NodeValue, 5)
        self.assertEqual(findResult.Node.Parent, tree.Root)
        self.assertEqual(findResult.NodeHasKey, False)
        self.assertEqual(findResult.ToLeft, False)

    def testFindMax(self):
        tree = BST(None)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(2, 2)

        result = tree.FinMinMax(tree.Root, True)

        self.assertEqual(result.NodeKey, 5)
        self.assertEqual(result.NodeValue, 5)
        self.assertEqual(result.Parent.NodeKey, 4)
        self.assertEqual(result.LeftChild, None)
        self.assertEqual(result.RightChild, None)

        tree.AddKeyValue(6, 6)

        parentMinNode = tree.FindNodeByKey(5).Node
        resultFromNode = tree.FinMinMax(parentMinNode, True)

        self.assertEqual(resultFromNode.NodeKey, 6)
        self.assertEqual(resultFromNode.NodeValue, 6)
        self.assertEqual(resultFromNode.Parent.NodeKey, 5)
        self.assertEqual(resultFromNode.LeftChild, None)
        self.assertEqual(resultFromNode.RightChild, None)

    def testFindMin(self):
        tree = BST(None)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(2, 2)

        result = tree.FinMinMax(tree.Root, False)

        self.assertEqual(result.NodeKey, 2)
        self.assertEqual(result.NodeValue, 2)
        self.assertEqual(result.Parent.NodeKey, 3)
        self.assertEqual(result.LeftChild, None)
        self.assertEqual(result.RightChild, None)

        tree.AddKeyValue(1, 1)

        parentMinNode = tree.FindNodeByKey(2).Node

        resultFromNode = tree.FinMinMax(parentMinNode, False)

        self.assertEqual(resultFromNode.NodeKey, 1)
        self.assertEqual(resultFromNode.NodeValue, 1)
        self.assertEqual(resultFromNode.Parent.NodeKey, 2)
        self.assertEqual(resultFromNode.LeftChild, None)
        self.assertEqual(resultFromNode.RightChild, None)

    def testDeleteRootNode(self):
        tree = BST(None)
        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.DeleteNodeByKey(1), True)
        self.assertEqual(tree.DeleteNodeByKey(1), False)

    def testDeleteNodeFromChildren(self):
        tree = BST(None)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(8, 8)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(12, 12)

        result = tree.DeleteNodeByKey(10)
        result2 = tree.DeleteNodeByKey(10)

        self.assertEqual(result, True)
        self.assertEqual(result2, False)
        self.assertEqual(tree.FindNodeByKey(10).NodeHasKey, False)
        self.assertEqual(tree.FindNodeByKey(7).Node.RightChild.NodeKey, 11)
        self.assertEqual(tree.FindNodeByKey(11).Node.Parent.NodeKey, 7)
        self.assertEqual(tree.FindNodeByKey(8).Node.Parent.NodeKey, 11)
        self.assertEqual(tree.FindNodeByKey(13).Node.Parent.NodeKey, 11)


if __name__ == "__main__":
    unittest.main()
