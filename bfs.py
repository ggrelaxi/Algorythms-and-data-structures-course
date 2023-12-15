class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.Parents = []


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.nodeCount = 0

    def AddVertex(self, v):
        if self.max_vertex == self.nodeCount:
            return False
        node = Vertex(v)
        emptyIndex = self.vertex.index(None)
        self.vertex[emptyIndex] = node
        self.nodeCount += 1
        return self.nodeCount - 1

        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        # pass

        # здесь и далее, параметры v -- индекс вершины
        # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        # pass
        self.vertex[v] = None
        self.nodeCount -= 1
        for i in range(self.max_vertex):
            self.m_adjacency[v][i] = 0
            self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        # False
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1]:
            return True
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        # pass
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        # pass
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        stack = []

        for i in range(len(self.vertex)):
            self.vertex[i].Hit = False

        def getEdges(nodeIdx):
            currentNodeReferences = self.m_adjacency[nodeIdx]
            currentNodeReferencesNodeIndex = []
            for i in range(len(currentNodeReferences)):
                ref = currentNodeReferences[i]
                if ref == 0:
                    continue
                else:
                    currentNodeReferencesNodeIndex.append(i)
            return currentNodeReferencesNodeIndex

        def iter(sourceIdx, dest, acc):
            currentNode = self.vertex[sourceIdx]
            if currentNode.Hit != True:
                currentNode.Hit = True
                acc.append(self.vertex[sourceIdx])

                currentNodeReferencesNodeIndex = getEdges(sourceIdx)
                if dest in currentNodeReferencesNodeIndex:
                    acc.append(self.vertex[dest])
                    return acc

                for i in range(len(currentNodeReferencesNodeIndex)):
                    currentRefNodeIndex = currentNodeReferencesNodeIndex[i]
                    if self.vertex[currentRefNodeIndex].Hit == False:
                        return iter(currentRefNodeIndex, dest, acc)

            acc.pop()

            if len(acc) == 0:
                return acc

            lastNodeFromAcc = acc[len(acc) - 1]

            return iter(self.vertex.index(lastNodeFromAcc), dest, acc)

        return iter(VFrom, VTo, stack)

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        queue = []

        for i in range(len(self.vertex)):
            self.vertex[i].Hit = False

        def getEdges(nodeIdx):
            currentNodeReferences = self.m_adjacency[nodeIdx]
            currentNodeReferencesNodeIndex = []
            for i in range(len(currentNodeReferences)):
                ref = currentNodeReferences[i]
                if ref == 0:
                    continue
                else:
                    currentNodeReferencesNodeIndex.append(i)
            return currentNodeReferencesNodeIndex

        def iter(sourceIdx):
            currentNode = self.vertex[sourceIdx]
            if sourceIdx == VTo:
                return [currentNode]
            currentNode.Hit = True

            currentNodeReferencesNodeIndex = getEdges(sourceIdx)

            for i in range(len(currentNodeReferencesNodeIndex)):
                currentRefNodeIndex = currentNodeReferencesNodeIndex[i]
                currentRefNode = self.vertex[currentRefNodeIndex]
                if currentRefNode.Hit == False:
                    if currentRefNodeIndex == VTo:
                        return [*currentNode.Parents, currentNode, currentRefNode]

                    self.vertex[currentRefNodeIndex].Hit = True
                    self.vertex[currentRefNodeIndex].Parents = [
                        *currentNode.Parents, currentNode]
                    queue.insert(0, currentRefNodeIndex)

            if len(queue) == 0:
                return queue

            lastQueueItem = queue.pop()

            return iter(lastQueueItem)

        return iter(VFrom)
