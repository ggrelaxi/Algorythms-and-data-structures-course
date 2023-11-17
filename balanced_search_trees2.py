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
        def iter(node, balanced):
            if node is None or not balanced:
                return [0, balanced]
            
            if node.LeftChild is not None and node.NodeKey <= node.LeftChild.NodeKey:
                return [node.Level, False]
            if node.RightChild is not None and node.NodeKey > node.RightChild.NodeKey:
                return [node.Level, False]
            
            leftHeight = iter(node.LeftChild, balanced)[0]
            rightHeight = iter(node.RightChild, balanced)[0]

            if abs(leftHeight - rightHeight) > 1:
                balanced = False

            return [max(leftHeight, rightHeight) + 1, balanced]

        return iter(root_node, True)[1]