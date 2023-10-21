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

        if findNode == self.Root:
            self.Root = None
            return True

        if findNode.NodeKey != key:
            return False

        parent = findNode.Parent
        leftChildren = findNode.LeftChild
        rightChildren = findNode.RightChild

        minNodeFromRightChildren = self.FinMinMax(rightChildren, False)
        candidateParent = minNodeFromRightChildren.Parent
        # лист в левой ветке узла приемника.
        if minNodeFromRightChildren.LeftChild is None and minNodeFromRightChildren.RightChild is None:
            if findNode == parent.LeftChild:
                parent.LeftChild = minNodeFromRightChildren
            if findNode == parent.RightChild:
                parent.RightChild = minNodeFromRightChildren

            if minNodeFromRightChildren == candidateParent.LeftChild:
                candidateParent.LeftChild = None
            if minNodeFromRightChildren == candidateParent.RightChild:
                candidateParent.RightChild = None

            minNodeFromRightChildren.LeftChild = leftChildren
            minNodeFromRightChildren.RightChild = rightChildren
            return True

        # узел только с правым потомком
        if minNodeFromRightChildren.LeftChild is None and minNodeFromRightChildren.RightChild is not None:
            if findNode == parent.LeftChild:
                parent.LeftChild = minNodeFromRightChildren
            if findNode == parent.RightChild:
                parent.RightChild = minNodeFromRightChildren

            if minNodeFromRightChildren == candidateParent.LeftChild:
                candidateParent.LeftChild = minNodeFromRightChildren.RightChild
                minNodeFromRightChildren.RightChild.parent = candidateParent.LeftChild
            if minNodeFromRightChildren == candidateParent.RightChild:
                candidateParent.RightChild = minNodeFromRightChildren.RightChild
                minNodeFromRightChildren.RightChild.parent = candidateParent.RightChild

            minNodeFromRightChildren.LeftChild = leftChildren
            minNodeFromRightChildren.RightChild = rightChildren
            leftChildren.Parent = minNodeFromRightChildren
            rightChildren.Parent = minNodeFromRightChildren
            minNodeFromRightChildren.Parent = parent
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
