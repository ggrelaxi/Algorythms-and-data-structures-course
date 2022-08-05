class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        nodes = []

        def iter(node, accumulator):
            accumulator.append(node)
            if len(node.Children) == 0:
                return

            for i in range(len(node.Children)):
                iter(node.Children[i], accumulator)

        iter(self.Root, nodes)

        return nodes

    def FindNodesByValue(self, val):
        nodes = []

        def iter(node, accumulator):
            if node.NodeValue == val:
                accumulator.append(node)
            if len(node.Children) == 0:
                return

            for i in range(len(node.Children)):
                iter(node.Children[i], accumulator)

        iter(self.Root, nodes)

        return nodes

    def MoveNode(self, OriginalNode, NewParent):
        originalParent = OriginalNode.Parent
        originalParent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)

    def Count(self):
        def iter(node):
            if len(node.Children) == 0:
                return 1

            innerCount = 0
            for i in range(len(node.Children)):
                innerCount += iter(node.Children[i])
            return innerCount + 1
        return iter(self.Root)

    def LeafCount(self):
        def iter(node):
            if len(node.Children) == 0:
                return 1

            innerCount = 0

            for i in range(len(node.Children)):
                innerCount += iter(node.Children[i])

            return innerCount

        return iter(self.Root)
