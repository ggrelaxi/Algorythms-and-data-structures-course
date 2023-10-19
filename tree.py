class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        # pass  # ваш код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if (NodeToDelete == self.Root):
            return
        parentNode = NodeToDelete.Parent
        deletedNodeIndex = parentNode.Children.index(NodeToDelete)
        parentNode.Children.pop(deletedNodeIndex)
        # pass  # ваш код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        listOfNodes = []

        if self.Root is None:
            return listOfNodes

        nodes = [self.Root]

        while (len(nodes) > 0):
            lastNode = nodes.pop(0)
            listOfNodes.append(lastNode)
            nodes.extend(lastNode.Children)

        return listOfNodes
        # ваш код выдачи всех узлов дерева в определённом порядке
        # return []

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []

        def iter(node, acc):
            if node.NodeValue == val:
                acc.append(node)
            for childNode in node.Children:
                iter(childNode, acc)
            return acc

        return iter(self.Root, [])
        # ваш код поиска узлов по значению
        # return []

    def MoveNode(self, OriginalNode, NewParent):
        prevParent = OriginalNode.Parent
        prevParent.Children.pop(prevParent.Children.index(OriginalNode))
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        # pass

    def Count(self):
        if self.Root is None:
            return 0

        def iter(node):
            if len(node.Children) == 0:
                return 1

            sum = 1
            for childNode in node.Children:
                sum = sum + iter(childNode)
            return sum

        return iter(self.Root)

    def LeafCount(self):
        def iter(node):
            if node is None:
                return 0
            if len(node.Children) == 0:
                return 1

            sum = 0
            for childNode in node.Children:
                sum += iter(childNode)

            return sum

        return iter(self.Root)
