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
        rootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(rootNode)

        level2firstNode = SimpleTreeNode('n1', newTree.Root)
        level2secondNode = SimpleTreeNode('n2', newTree.Root)
        level2ThirdNode = SimpleTreeNode('n3', newTree.Root)

        newTree.AddChild(newTree.Root, level2firstNode)
        newTree.AddChild(newTree.Root, level2secondNode)
        newTree.AddChild(newTree.Root, level2ThirdNode)

        level3firstNode = SimpleTreeNode('n12', level2firstNode)
        level3secondNode = SimpleTreeNode('n13', level2firstNode)

        newTree.AddChild(level2firstNode, level3firstNode)
        newTree.AddChild(level2firstNode, level3secondNode)

        self.assertEqual(newTree.Count(), 6)

        leve3thirdNode = SimpleTreeNode('n21', level2secondNode)
        newTree.AddChild(level2secondNode, leve3thirdNode)

        self.assertEqual(newTree.Count(), 7)
        self.assertEqual(newTree.LeafCount(), 4)

        newTree.MoveNode(level2secondNode, level2ThirdNode)

        self.assertEqual(newTree.Count(), 7)
        self.assertEqual(newTree.LeafCount(), 3)
        self.assertFalse(level2secondNode in newTree.Root.Children)

        newTree.DeleteNode(leve3thirdNode)

        self.assertEqual(newTree.Count(), 6)
        self.assertEqual(newTree.LeafCount(), 3)

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
