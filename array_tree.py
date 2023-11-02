class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        root = self.Tree[0]

        def iter(node, index):
            if node is None:
                return -index
            if node == key:
                return index

            childIndex = (2 * index) + 2 if node < key else (2 * index) + 1

            if childIndex >= len(self.Tree):
                return None
            if node == key:
                return index
            if node < key:
                return iter(self.Tree[childIndex], childIndex)
            if node > key:
                return iter(self.Tree[childIndex], childIndex)

        result = iter(root, 0)
        if result == 0 and root is None:
            return -1
        return result  # не найден

    def AddKey(self, key):
        def iter(node, index):
            if node is None:
                self.Tree[index] = key
                return index

            childIndex = (2 * index) + 2 if node < key else (2 * index) + 1

            if childIndex >= len(self.Tree):
                return -1
            if node == key:
                return index
            if node < key:
                return iter(self.Tree[childIndex], childIndex)
            if node > key:
                return iter(self.Tree[childIndex], childIndex)

        return iter(self.Tree[0], 0)
        # индекс добавленного/существующего ключа или -1 если не удалось
