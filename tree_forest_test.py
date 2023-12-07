import unittest
from tree_forest import SimpleTree, SimpleTreeNode


class SimpleTreeTest(unittest.TestCase):
    def testAddRoot(self):
        # проверка пустого корня в новом дереве
        newTree = SimpleTree(None)

        self.assertEqual(newTree.Root, None)

        # проверка корректного добавления корня дерева
        newRootNode = SimpleTreeNode(1, None)
        newTree2 = SimpleTree(newRootNode)
        self.assertEqual(newTree2.Root, newRootNode)
        self.assertEqual(newRootNode.Parent, None)

    def testAddChild(self):
        # проверка добавления дочернего узла для корня
        newRootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(newRootNode)
        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)

        self.assertTrue(newChildNode in newRootNode.Children)
        self.assertEqual(newChildNode.Parent, newRootNode)

    def testDeleteNode(self):
        # проверка удаления корневого узла.

        newRootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(newRootNode)
        newTree.DeleteNode(newRootNode)

        self.assertEqual(newTree.Root, newRootNode)

        # проверка удаления удаления узла - отстутсвие в поле Children родителя.

        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)
        newTree.DeleteNode(newChildNode)

        self.assertTrue(newChildNode not in newRootNode.Children)
        self.assertTrue(newChildNode.Parent is None)
        self.assertEqual(newTree.Count(), 1)
        self.assertEqual(newTree.LeafCount(), 1)

        newChildNode2 = SimpleTreeNode(3, newRootNode)
        newChildNode3 = SimpleTreeNode(4, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)
        newTree.AddChild(newRootNode, newChildNode2)
        newTree.AddChild(newRootNode, newChildNode3)
        self.assertTrue(newTree.Count(), 4)
        newTree.MoveNode(newChildNode, newChildNode3)
        newTree.DeleteNode(newChildNode3)

        self.assertEqual(newTree.LeafCount(), 1)
        self.assertEqual(newTree.Count(), 2)
        self.assertTrue(newChildNode3.Parent is not newRootNode)
        self.assertTrue(newChildNode3 not in newRootNode.Children)

        newTree.DeleteNode(newChildNode2)

        self.assertEqual(newTree.LeafCount(), 1)
        self.assertEqual(newTree.Count(), 1)

    def testGetListOfNodes(self):
        # получения списка узлов, в дереве из одного узла

        newRootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(newRootNode)

        self.assertEqual(len(newTree.GetAllNodes()), 1)
        self.assertEqual(newTree.GetAllNodes(), [newRootNode])

        # получения списка узлов, в дереве из двух узлов
        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)

        self.assertEqual(len(newTree.GetAllNodes()), 2)
        self.assertEqual(newTree.GetAllNodes(), [newRootNode, newChildNode])

        # получения списка узлов, в дереве из трех узлов
        newChildNode2 = SimpleTreeNode(3, newChildNode)
        newChildNode3 = SimpleTreeNode(4, newChildNode)
        newTree.AddChild(newChildNode, newChildNode2)
        newTree.AddChild(newChildNode, newChildNode3)

        self.assertEqual(len(newTree.GetAllNodes()), 4)
        self.assertEqual(newTree.GetAllNodes(), [
                         newRootNode, newChildNode, newChildNode2, newChildNode3])

    def testFindNodeByValue(self):
        # Проверка поиска узла по значения, в дереве с одним узлом
        newRootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(newRootNode)

        self.assertEqual(newTree.FindNodesByValue(0), [])
        self.assertEqual(newTree.FindNodesByValue(1), [newRootNode])

        # Проверка поиска узла по значения, в дереве из нескольких элементов
        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)

        self.assertEqual(newTree.FindNodesByValue(2), [newChildNode])

        newChildNode2 = SimpleTreeNode(1, newRootNode)
        newTree.AddChild(newRootNode, newChildNode2)

        self.assertEqual(newTree.FindNodesByValue(1),
                         [newRootNode, newChildNode2])

    def testMoveNode(self):
        # проверка перемещения узла
        newRootNode = SimpleTreeNode(1, None)
        newTree = SimpleTree(newRootNode)
        newChildNode = SimpleTreeNode(2, newRootNode)
        newChildNode2 = SimpleTreeNode(3, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)
        newTree.AddChild(newRootNode, newChildNode2)

        newTree.MoveNode(newChildNode, newChildNode2)

        self.assertEqual(newTree.Count(), 3)
        self.assertEqual(newTree.LeafCount(), 1)
        self.assertTrue(newChildNode not in newRootNode.Children)
        self.assertTrue(newChildNode.Parent != newRootNode)
        self.assertTrue(newChildNode.Parent == newChildNode2)
        self.assertTrue(newChildNode in newChildNode2.Children)

    def testCountNodes(self):
        # проверка пустого дерева
        newTree = SimpleTree(None)

        self.assertEqual(newTree.Count(), 0)

        # проверка дерева с одним корнем
        newRootNode = SimpleTreeNode(1, None)
        newTree.Root = newRootNode

        self.assertEqual(newTree.Count(), 1)

        # проверка дерева с дочерними узлами

        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)

        self.assertEqual(newTree.Count(), 2)

        newChildNode2 = SimpleTreeNode(3, newRootNode)
        newTree.AddChild(newRootNode, newChildNode2)

        self.assertEqual(newTree.Count(), 3)

    def testLeafCount(self):
        # проверка пустого дерева
        newTree = SimpleTree(None)

        self.assertEqual(newTree.LeafCount(), 0)

        # проверка дерева с одним корнем
        newRootNode = SimpleTreeNode(1, None)
        newTree.Root = newRootNode

        self.assertEqual(newTree.LeafCount(), 1)

        # проверка с одним дочерним узлом

        newChildNode = SimpleTreeNode(2, newRootNode)
        newTree.AddChild(newRootNode, newChildNode)

        self.assertEqual(newTree.LeafCount(), 1)

        # проверка с более чем 1 дочерним узлом

        newChildNode2 = SimpleTreeNode(3, newRootNode)
        newTree.AddChild(newRootNode, newChildNode2)

        self.assertEqual(newTree.LeafCount(), 2)

    def testEvenTrees(self):
        newTree = SimpleTree(None)

        newRootNode = SimpleTreeNode(1, None)
        newTree.Root = newRootNode

        sixNode = SimpleTreeNode(6, newRootNode)
        threeNode = SimpleTreeNode(3, newRootNode)
        twoNode = SimpleTreeNode(2, newRootNode)

        newTree.AddChild(newRootNode, sixNode)
        newTree.AddChild(newRootNode, threeNode)
        newTree.AddChild(newRootNode, twoNode)

        eigthNode = SimpleTreeNode(8, sixNode)
        newTree.AddChild(sixNode, eigthNode)

        fourNode = SimpleTreeNode(4, threeNode)
        newTree.AddChild(threeNode, fourNode)

        sevenNode = SimpleTreeNode(7, twoNode)
        newTree.AddChild(twoNode, sevenNode)

        fiveNode = SimpleTreeNode(5, twoNode)
        newTree.AddChild(twoNode, fiveNode)

        tenNode = SimpleTreeNode(10, eigthNode)
        newTree.AddChild(eigthNode, tenNode)

        nineNode = SimpleTreeNode(9, eigthNode)
        newTree.AddChild(eigthNode, nineNode)

        result = [newRootNode, threeNode, newRootNode, sixNode]

        self.assertEqual(newTree.EvenTrees(), result)


if __name__ == "__main__":
    unittest.main()
