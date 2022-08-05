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
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)
        newChildNode = SimpleTreeNode(2, newTree.Root)
        newTree.AddChild(newTree.Root, newChildNode)
        newTree.DeleteNode(newChildNode)

        self.assertFalse(newChildNode in newTree.Root.Children)

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

        self.assertEqual(newTree.LeafCount(), 3)

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
