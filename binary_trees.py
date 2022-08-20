class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        def iter(node, s_result):
            if node is None:
                return s_result

            s_result.Node = node

            if node.NodeKey == key:
                s_result.NodeHasKey = True
                s_result.ToLeft = False
                return s_result

            left = node.LeftChild
            right = node.RightChild

            if node.NodeKey > key and left is not None:
                return iter(left, s_result)
            elif node.NodeKey > key and left is None:
                s_result.ToLeft = True
                s_result.NodeHasKey = False
                return s_result
            elif node.NodeKey <= key and right is not None:
                return iter(right, s_result)
            elif node.NodeKey <= key and right is None:
                s_result.ToLeft = False
                s_result.NodeHasKey = False
                return s_result

        return iter(self.Root, BSTFind())

    def AddKeyValue(self, key, val):
        search_result = self.FindNodeByKey(key)

        if search_result.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        if search_result.Node.NodeKey == key:
            return False

        if search_result.Node.NodeKey >= key:
            search_result.Node.LeftChild = BSTNode(
                key, val, search_result.Node)
            return True
        elif search_result.Node.NodeKey < key:
            search_result.Node.RightChild = BSTNode(
                key, val, search_result.Node)
            return True

    def FinMinMax(self, FromNode, FindMax):
        def iter(node):
            if FindMax == True:
                if node.RightChild is None:
                    return node
                else:
                    return iter(node.RightChild)
            else:
                if node.LeftChild is None:
                    return node
                else:
                    return iter(node.LeftChild)
        return iter(FromNode)

    def DeleteNodeByKey(self, key):
        def iter(node):
            if node.LeftChild is not None:
                return iter(node.LeftChild)
            return node

        current_node = self.FindNodeByKey(key)
        if current_node.NodeHasKey == False:
            return False

        left = current_node.Node.LeftChild
        right = current_node.Node.RightChild
        current_key = current_node.Node.NodeKey
        parent = current_node.Node.Parent

        if left is None and right is None:
            if parent is None:
                self.Root = None
                return True
            if parent.NodeKey >= current_key:
                parent.LeftChild = None
                return True
            parent.RightChild = None
            return True

        elif left is not None and right is None:
            if parent is None:
                self.Root = left
                left.Parent = None
                return True
            parent.LeftChild = left
            left.Parent = parent
            return True
        elif left is None and right is not None:
            if parent is None:
                self.Root = right
                right.Parent = None
                return True
            parent.RightChild = right
            right.Parent = parent
            return True

        else:
            candidate = iter(right)
            if candidate.LeftChild is None and candidate.RightChild is None:
                candidate.LeftChild = left
                left.Parent = candidate
                if right != candidate:
                    candidate.RightChild = right
                    right.Parent = candidate
                candidate.Parent.LeftChild = None
                if parent is None:
                    self.Root = candidate
                    self.Root.Parent = None
                else:
                    parent.RightChild = candidate
                return True
            elif candidate.LeftChild is None and candidate.RightChild is not None:
                candidate.LeftChild = left
                if right != candidate:
                    candidate.RightChild = right
                    right.Parent = candidate

                left.Parent = candidate
                candidate.Parent = parent
                if parent is None:
                    self.Root = candidate
                else:
                    parent.RightChild = candidate
                return True

    def Count(self):
        def iter(node):
            if node is None:
                return 0
            leftChildren = node.LeftChild
            rightChildren = node.RightChild

            leftLength = 0
            rightLength = 0

            if leftChildren is not None:
                leftLength = iter(leftChildren)

            if rightChildren is not None:
                rightLength = iter(rightChildren)

            return 1 + leftLength + rightLength
        return iter(self.Root)
