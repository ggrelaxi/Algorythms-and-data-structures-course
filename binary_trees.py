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
        def iter(node):
            if node is None:
                return BSTFind()

            result = BSTFind()
            result.Node = node

            if node.NodeKey == key:
                result.NodeHasKey = True

            if key < node.NodeKey:
                if node.LeftChild is not None:
                    return iter(node.LeftChild)
                else:
                    result.ToLeft = True

            if key > node.NodeKey:
                if node.RightChild is not None:
                    return iter(node.RightChild)

            return result

        return iter(self.Root)
        # ищем в дереве узел и сопутствующую информацию по ключу
        # return None # возвращает BSTFind

    def AddKeyValue(self, key, val):
        find = self.FindNodeByKey(key)

        if find.Node is None:
            self.Root = BSTNode(key, val, None)
            return True

        if find.NodeHasKey == True:
            return False

        if find.NodeHasKey == False:
            newNode = BSTNode(key, val, find.Node)
            if find.ToLeft == True:
                find.Node.LeftChild = newNode
            else:
                find.Node.RightChild = newNode
            return True

        # добавляем ключ-значение в дерево
        # return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        def iter(node):
            if FindMax == True:
                if node.RightChild is None:
                    return node
                return iter(node.RightChild)
            else:
                if node.LeftChild is None:
                    return node
                return iter(node.LeftChild)

        return iter(FromNode)

        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        # return None

    def DeleteNodeByKey(self, key):
        findNode = self.FindNodeByKey(key).Node

        if findNode is None:
            return False

        if findNode == self.Root and findNode.NodeKey == key:
            self.Root = None
            return True

        if findNode.NodeKey != key:
            return False

        parent = findNode.Parent
        leftChildren = findNode.LeftChild
        rightChildren = findNode.RightChild

        # удаляем листовой узел
        if leftChildren is None and rightChildren is None:
            findNode.Parent = None
            if findNode == parent.LeftChild:
                parent.LeftChild = None
            if findNode == parent.RightChild:
                parent.RightChild = None
            return True

        # удаляем узел с одним левым потомком
        if leftChildren is not None and rightChildren is None:
            findNode.Parent = None
            findNode.LeftChild = None
            leftChildren.Parent = parent
            if findNode == parent.LeftChild:
                parent.LeftChild = leftChildren
            if findNode == parent.RightChild:
                parent.LeftChild = leftChildren
            return True

        # Удаляем узел с одним правым потомком
        if leftChildren is None and rightChildren is not None:
            findNode.Parent = None
            findNode.RightChild = None
            rightChildren.Parent = parent
            if findNode == parent.LeftChild:
                parent.LeftChild = rightChildren
            if findNode == parent.RightChild:
                parent.LeftChild = rightChildren
            return True

        minNodeFromRightChildren = self.FinMinMax(rightChildren, False)

        minNodeLeftChild = minNodeFromRightChildren.LeftChild
        minNodeRightChild = minNodeFromRightChildren.RightChild
        minNodeParent = minNodeFromRightChildren.Parent

        if findNode == parent.LeftChild:
            parent.LeftChild = minNodeFromRightChildren
        if findNode == parent.RightChild:
            parent.RightChild = minNodeFromRightChildren
        findNode.Parent = None
        findNode.LeftChild = None
        findNode.RightChild = None

        minNodeFromRightChildren.Parent = parent
        leftChildren.Parent = minNodeFromRightChildren
        rightChildren.Parent = minNodeFromRightChildren
        minNodeFromRightChildren.LeftChild = leftChildren
        minNodeFromRightChildren.RightChild = rightChildren

        minNodeParent.LeftChild = minNodeRightChild
        if minNodeRightChild is not None:
            minNodeRightChild.Parent = minNodeParent
        return True

        # удаляем узел по ключу
        # return False  # если узел не найден

    def Count(self):
        def iter(node):
            if node is None:
                return 0
            return 1 + iter(node.LeftChild) + iter(node.RightChild)

        return iter(self.Root)
        # количество узлов в дереве

    def WideAllNodes(self):
        nodes = []
        q = []

        if self.Root is not None:
            q.append(self.Root)

        def iter(q, acc):
            if len(q) == 0:
                return

            node = q.pop()
            acc.append(node)

            leftChild = node.LeftChild
            rightChild = node.RightChild

            if (leftChild is not None):
                q.insert(0, leftChild)
            if (rightChild is not None):
                q.insert(0, rightChild)

            iter(q, acc)

        iter(q, nodes)

        return nodes

    def DeepAllNodes(self, order):
        nodes = []

        def iter(node, order):
            if node is None:
                return

            leftChild = node.LeftChild
            rigthChild = node.RightChild

            if order == 0:
                if leftChild is not None:
                    iter(leftChild, order)

                nodes.append(node)

                if rigthChild is not None:
                    iter(rigthChild, order)

            if order == 1:
                if leftChild is not None:
                    iter(leftChild, order)
                if rigthChild is not None:
                    iter(rigthChild, order)
                nodes.append(node)

            if order == 2:
                nodes.append(node)

                if leftChild is not None:
                    iter(leftChild, order)

                if rigthChild is not None:
                    iter(rigthChild, order)

        iter(self.Root, order)

        return nodes
