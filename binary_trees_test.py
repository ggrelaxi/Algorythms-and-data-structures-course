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

    def testAddExistedKey(self):
        tree = BST(None)

        # не совсем понятно по формулировке задания, что должна возвращать функция, если ключ существует
        self.assertEqual(tree.AddKeyValue(1, 1), True)
        self.assertEqual(tree.AddKeyValue(1, 1), False)
        self.assertEqual(tree.Count(), 1)

    def testAddLeftChild(self):
        tree = BST(None)

        tree.AddKeyValue(2, 2)
        self.assertEqual(tree.FindNodeByKey(2).Node.LeftChild, None)
        self.assertEqual(tree.FindNodeByKey(1).ToLeft, True)
        self.assertEqual(tree.AddKeyValue(1, 1), True)
        self.assertEqual(tree.Count(), 2)

        self.assertEqual(tree.FindNodeByKey(1).Node.NodeKey, 1)
        self.assertEqual(tree.FindNodeByKey(1).Node.NodeValue, 1)
        self.assertEqual(tree.FindNodeByKey(1).Node.Parent,
                         tree.FindNodeByKey(2).Node)
        self.assertEqual(tree.Root.LeftChild, tree.FindNodeByKey(1).Node)

    def testAddRightChild(self):
        tree = BST(None)
        tree.AddKeyValue(2, 2)

        self.assertEqual(tree.FindNodeByKey(2).Node.RightChild, None)
        self.assertEqual(tree.FindNodeByKey(3).ToLeft, False)
        self.assertEqual(tree.AddKeyValue(3, 3), True)
        self.assertEqual(tree.Count(), 2)

        self.assertEqual(tree.FindNodeByKey(3).Node.NodeKey, 3)
        self.assertEqual(tree.FindNodeByKey(3).Node.NodeValue, 3)
        self.assertEqual(tree.FindNodeByKey(3).Node.Parent,
                         tree.FindNodeByKey(2).Node)
        self.assertEqual(tree.FindNodeByKey(3).Node.Parent,
                         tree.FindNodeByKey(2).Node)

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
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(3, 3)

        result = tree.FinMinMax(tree.Root, False)
        self.assertEqual(result.NodeKey, 2)
        self.assertEqual(result.NodeValue, 2)
        self.assertEqual(result.Parent.NodeKey, 4)
        self.assertEqual(result.LeftChild, None)
        self.assertEqual(result.RightChild.NodeKey, 3)

        tree.AddKeyValue(1, 1)

        parentMinNode = tree.FindNodeByKey(2).Node

        resultFromNode = tree.FinMinMax(parentMinNode, False)

        self.assertEqual(resultFromNode.NodeKey, 1)
        self.assertEqual(resultFromNode.NodeValue, 1)
        self.assertEqual(resultFromNode.Parent.NodeKey, 2)
        self.assertEqual(resultFromNode.Parent.LeftChild, resultFromNode)
        self.assertEqual(resultFromNode.LeftChild, None)
        self.assertEqual(resultFromNode.RightChild, None)

    def testDeleteRootNode(self):
        tree = BST(None)
        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.DeleteNodeByKey(1), True)
        self.assertEqual(tree.DeleteNodeByKey(1), False)

    # def testDeleteNodeFromChildren(self):
    #     tree = BST(None)
    #     tree.AddKeyValue(4, 4)
    #     tree.AddKeyValue(3, 3)
    #     tree.AddKeyValue(7, 7)
    #     tree.AddKeyValue(10, 10)
    #     tree.AddKeyValue(8, 8)
    #     tree.AddKeyValue(13, 13)
    #     tree.AddKeyValue(11, 11)
    #     tree.AddKeyValue(12, 12)

    #     result = tree.DeleteNodeByKey(10)
    #     result2 = tree.DeleteNodeByKey(10)

    #     self.assertEqual(result, True)
    #     self.assertEqual(result2, False)
    #     self.assertEqual(tree.FindNodeByKey(10).NodeHasKey, False)
    #     self.assertEqual(result.Parent, None)
    #     self.assertEqual(result.LeftChild, None)
    #     self.assertEqual(result.RightChild, None)

    #     self.assertEqual(tree.FindNodeByKey(7).Node.RightChild.NodeKey, 11)
    #     self.assertEqual(tree.FindNodeByKey(11).Node.Parent.NodeKey, 7)
    #     self.assertEqual(tree.FindNodeByKey(8).Node.Parent.NodeKey, 11)
    #     self.assertEqual(tree.FindNodeByKey(13).Node.Parent.NodeKey, 11)

    # Проверка удаления корневой ноды
    def testDeletedRootNode(self):
        tree = BST(None)

        self.assertEqual(tree.DeleteNodeByKey(1), False)

        tree.AddKeyValue(1, 1)

        rootNode = tree.FindNodeByKey(1)

        self.assertEqual(tree.DeleteNodeByKey(1), True)
        self.assertEqual(tree.DeleteNodeByKey(1), False)
        self.assertEqual(tree.Count(), 0)
        self.assertEqual(tree.Root, None)
        self.assertEqual(rootNode.Node.Parent, None)

    # Проверка удаления листовой ноды
    def testListNode(self):
        tree = BST(None)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(1, 1)

        listNode = tree.FindNodeByKey(1).Node
        rootNode = tree.FindNodeByKey(2).Node

        self.assertEqual(tree.DeleteNodeByKey(1), True)
        self.assertEqual(tree.DeleteNodeByKey(1), False)
        self.assertEqual(rootNode.LeftChild, None)
        self.assertEqual(listNode.Parent, None)
        self.assertEqual(tree.Count(), 1)

    # Проверка удаления ноды с одним левым потомком
    def testDeletedNodeWithLeftChild(self):
        tree = BST(None)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(1, 1)

        deletedNode = tree.FindNodeByKey(2).Node
        parentNode = tree.FindNodeByKey(3).Node
        leftChildNode = tree.FindNodeByKey(1).Node

        self.assertEqual(tree.DeleteNodeByKey(2), True)
        self.assertEqual(tree.DeleteNodeByKey(2), False)
        self.assertEqual(deletedNode.Parent, None)
        self.assertEqual(deletedNode.LeftChild, None)
        self.assertEqual(parentNode.LeftChild, leftChildNode)
        self.assertEqual(leftChildNode.Parent, parentNode)
        self.assertEqual(tree.Count(), 2)

    # Проверка удаления узла с двумя потомками
    def testDeletedNodeWithChildren(self):
        tree = BST(None)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(8, 8)
        tree.AddKeyValue(7, 7)

        parent = tree.FindNodeByKey(3).Node
        deleted = tree.FindNodeByKey(6).Node
        fiveNode = tree.FindNodeByKey(5).Node
        eightNode = tree.FindNodeByKey(8).Node
        sevenNode = tree.FindNodeByKey(7).Node

        self.assertEqual(tree.DeleteNodeByKey(6), True)
        self.assertEqual(tree.DeleteNodeByKey(6), False)
        self.assertEqual(parent.RightChild, sevenNode)
        self.assertEqual(sevenNode.Parent, parent)
        self.assertEqual(sevenNode.LeftChild, fiveNode)
        self.assertEqual(fiveNode.Parent, sevenNode)
        self.assertEqual(sevenNode.RightChild, eightNode)
        self.assertEqual(eightNode.Parent, sevenNode)
        self.assertEqual(eightNode.LeftChild, None)
        self.assertEqual(deleted.Parent, None)
        self.assertEqual(deleted.LeftChild, None)
        self.assertEqual(deleted.RightChild, None)

    def testWideAllNodes(self):
        tree = BST(None)

        self.assertEqual(len(tree.WideAllNodes()), 0)
        self.assertEqual(tree.WideAllNodes(), [])

        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(4, 4)

        self.assertEqual(len(tree.WideAllNodes()), 3)
        self.assertEqual(tree.WideAllNodes(), [tree.FindNodeByKey(
            3).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(4).Node])

        tree.AddKeyValue(1, 1)
        self.assertEqual(len(tree.WideAllNodes()), 4)
        self.assertEqual(tree.WideAllNodes(), [tree.FindNodeByKey(
            3).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(1).Node])

    def testDeepAllNodes(self):
        tree = BST(None)

        self.assertEqual(len(tree.DeepAllNodes(0)), 0)
        self.assertEqual(tree.DeepAllNodes(0), [])
        self.assertEqual(len(tree.DeepAllNodes(1)), 0)
        self.assertEqual(tree.DeepAllNodes(1), [])
        self.assertEqual(len(tree.DeepAllNodes(2)), 0)
        self.assertEqual(tree.DeepAllNodes(2), [])

        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(4, 4)

        self.assertEqual(len(tree.DeepAllNodes(0)), 3)
        self.assertEqual(tree.DeepAllNodes(0), [tree.FindNodeByKey(
            2).Node, tree.FindNodeByKey(3).Node, tree.FindNodeByKey(4).Node])

        self.assertEqual(len(tree.DeepAllNodes(1)), 3)
        self.assertEqual(tree.DeepAllNodes(1), [tree.FindNodeByKey(
            2).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(3).Node])

        self.assertEqual(len(tree.DeepAllNodes(2)), 3)
        self.assertEqual(tree.DeepAllNodes(2), [tree.FindNodeByKey(
            3).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(4).Node])

    def testDeepAllNodesInner(self):
        tree = BST(None)

        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(1, 1)

        self.assertEqual(len(tree.DeepAllNodes(0)), 5)
        self.assertEqual(tree.DeepAllNodes(0), [tree.FindNodeByKey(
            1).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(5).Node, tree.FindNodeByKey(6).Node])
        self.assertEqual(len(tree.DeepAllNodes(1)), 5)
        self.assertEqual(tree.DeepAllNodes(1), [tree.FindNodeByKey(
            1).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(6).Node, tree.FindNodeByKey(5).Node])
        self.assertEqual(len(tree.DeepAllNodes(2)), 5)
        self.assertEqual(tree.DeepAllNodes(2), [tree.FindNodeByKey(
            5).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(1).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(6).Node])


    def testReverseTree(self):
        tree = BST(None)

        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(1, 1)

        self.assertEqual(tree.Reverse(),[tree.FindNodeByKey(
            5).Node, tree.FindNodeByKey(2).Node, tree.FindNodeByKey(1).Node, tree.FindNodeByKey(4).Node, tree.FindNodeByKey(6).Node])

if __name__ == "__main__":
    unittest.main()
