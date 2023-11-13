class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, a):
        a.sort()
        def iter(part, parent, level):
            if len(part) == 0:
                return None
            
            middleIndex = len(part) // 2
            rootItem = part[middleIndex]

            newNode = BSTNode(rootItem, parent)
            newNode.Level = level

            newNode.LeftChild = iter(part[:middleIndex], newNode, level + 1)
            newNode.RightChild = iter(part[middleIndex + 1:], newNode, level + 1)

            return newNode

        self.Root = iter(a, None, 0)
        return self.Root
	# создаём дерево с нуля из неотсортированного массива a
	# ...      

    def IsBalanced(self, root_node):
        def iter(node):
            if node is None:
                return True
            if node.LeftChild is not None and node.LeftChild.NodeKey >= node.NodeKey:
                return False
            if node.RightChild is not None and node.RightChild.NodeKey < node.nodeKey:
                return False
            
            iter(node.LeftChild)
            iter(node.RightChild)

        return iter(root_node)