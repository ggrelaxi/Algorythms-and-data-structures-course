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
            if node == None:
                return s_result

            s_result.Node = node

            if node.NodeKey == key:
                s_result.NodeHasKey = True
                return s_result

            left = node.LeftChild
            right = node.RightChild

            s_result.NodeHasKey = False

            if node.NodeKey > key and left != None:
                return iter(left, s_result)
            elif node.NodeKey > key and left == None:
                s_result.ToLeft = True
                return s_result
            elif node.NodeKey < key and right != None:
                return iter(right, s_result)
            elif node.NodeKey < key and right == None:
                s_result.ToLeft = False
                return s_result

        return iter(self.Root, BSTFind())

    def AddKeyValue(self, key, val):
        search_result = self.FindNodeByKey(key)

        if search_result.Node == None:
            self.Root = BSTNode(key, val, None)
            return True
        if search_result.Node.NodeKey == key:
            return False

        if search_result.Node.NodeKey > key:
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
                if node.RightChild == None:
                    return node.NodeKey
                else:
                    return iter(node.RightChild)
            else:
                if node.LeftChild == None:
                    return node.NodeKey
                else:
                    return iter(node.LeftChild)
        return iter(FromNode)

    def DeleteNodeByKey(self, key):
        def iter(node):
            if node.LeftChild == None and node.RightChild == None:
                return node
            elif node.LeftChild == None and node.RightChild != None:
                return node
            return iter(node.LeftChild)

        current_node = self.FindNodeByKey(key)

        if current_node.Node == None:
            return False

        left = current_node.Node.LeftChild
        right = current_node.Node.RightChild
        current_key = current_node.Node.NodeKey
        parent = current_node.Node.Parent

        if parent == None and key == current_key:
            self.Root = None
            return True

        parent_key = current_node.Node.Parent.NodeKey

        if left == None and right == None:
            if parent_key > current_key:
                parent.LeftChild = None
                return True
            else:
                parent.RightChild = None
                return True
        elif left != None and right == None:
            parent.LeftChild = right
            right.Parent = parent
            return True
        elif left == None and right != None:
            parent.RightChild = right
            right.Parent = parent
            return True
        else:
            candidate = iter(right)
            if candidate.LeftChild == None and candidate.RightChild == None:
                candidate.LeftChild = left
                candidate.RightChild = right
                parent.RightChild = candidate
                return True
            else:
                candidate.LeftChild = current_node.LeftChild
                parent.RightChild = candidate
                return True

    def Count(self):
        def iter(node):
            if node == None:
                return 0

            left = node.LeftChild
            right = node.RightChild

            return 1 + iter(left) + iter(right)
        return iter(self.Root)
