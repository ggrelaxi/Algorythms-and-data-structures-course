class Vertex:

    def __init__(self, val):
        self.Value = val


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
        self.vertex.append(node)
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
