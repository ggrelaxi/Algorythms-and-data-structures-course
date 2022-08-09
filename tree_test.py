from hashlib import new
from logging import root
import unittest
from tree import SimpleTree, SimpleTreeNode


class SimpleTreeTest(unittest.TestCase):
    def testAddRootNode(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)

        self.assertEqual(newTree.Root, rootNode)

    def testAddNewNodeToCurrent(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newTree.AddChild(newTree.Root, newChildNode)

        self.assertTrue(newChildNode in newTree.Root.Children)

    def testDeleteNotRootNode(self):
        root = SimpleTreeNode(0, None)
        tree = SimpleTree(root)

        n1 = SimpleTreeNode(1, root)
        tree.AddChild(root, n1)
        n2 = SimpleTreeNode(2, root)
        tree.AddChild(root, n2)
        n3 = SimpleTreeNode(3, root)
        tree.AddChild(root, n3)
        n12 = SimpleTreeNode(2, None)
        tree.AddChild(n1, n12)
        n13 = SimpleTreeNode(3, None)
        tree.AddChild(n1, n13)
        n21 = SimpleTreeNode(4, None)
        tree.AddChild(n2, n21)

        tree.MoveNode(n2, n3)
        tree.DeleteNode(n21)

    def testGetAllNode(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newInnerNode = SimpleTreeNode(3, newChildNode)
        newTree.AddChild(newTree.Root, newChildNode)
        newTree.AddChild(newChildNode, newInnerNode)

        self.assertEqual(newTree.GetAllNodes(), [
                         rootNode, newChildNode, newInnerNode])

    def testFindNodesByValue(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newInnerNode = SimpleTreeNode(3, newChildNode)
        newSecondInnerNode = SimpleTreeNode(3, newChildNode)
        newThirdInnerNode = SimpleTreeNode(4, newChildNode)
        newTree.AddChild(newTree.Root, newChildNode)

        newTree.AddChild(newChildNode, newInnerNode)

        newTree.AddChild(newChildNode, newSecondInnerNode)

        newTree.AddChild(newChildNode, newThirdInnerNode)

        self.assertEqual(newTree.FindNodesByValue(
            3), [newInnerNode, newSecondInnerNode])

    def testCount(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newInnerNode = SimpleTreeNode(3, newChildNode)

        newSecondInnerNode = SimpleTreeNode(3, newChildNode)
        newThirdInnerNode = SimpleTreeNode(4, newChildNode)
        newTree.AddChild(newTree.Root, newChildNode)
        newTree.AddChild(newChildNode, newInnerNode)

        self.assertEqual(newTree.Count(), 3)

        newTree.AddChild(newChildNode, newSecondInnerNode)
        newTree.AddChild(newChildNode, newThirdInnerNode)
        self.assertEqual(newTree.Count(), 5)

    def testLeafsCount(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newInnerNode = SimpleTreeNode(3, newChildNode)
        newSecondInnerNode = SimpleTreeNode(3, newChildNode)
        newThirdInnerNode = SimpleTreeNode(4, newChildNode)
        newTree.AddChild(newTree.Root, newChildNode)

        newTree.AddChild(newChildNode, newInnerNode)

        newTree.AddChild(newChildNode, newSecondInnerNode)

        newTree.AddChild(newChildNode, newThirdInnerNode)

        # self.assertEqual(newTree.Count(), 6)

    def testMoveNode(self):
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newInnerNode = SimpleTreeNode(3, newChildNode)
        newSecondInnerNode = SimpleTreeNode(3, newChildNode)
        newThirdInnerNode = SimpleTreeNode(4, newChildNode)
        newTree.AddChild(newTree.Root, newChildNode)

        newTree.AddChild(newChildNode, newInnerNode)

        newTree.AddChild(newChildNode, newSecondInnerNode)

        newTree.AddChild(newChildNode, newThirdInnerNode)

        newTree.MoveNode(newThirdInnerNode, rootNode)

        self.assertTrue(newThirdInnerNode in rootNode.Children)
        self.assertTrue(newThirdInnerNode not in newChildNode.Children)


if __name__ == "__main__":
    unittest.main()
