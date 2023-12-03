import unittest
from graph import SimpleGraph, Vertex


class GenerateHeapTest(unittest.TestCase):
    def testAddVertex(self):
        emptyGraph = SimpleGraph(0)

        self.assertEqual(emptyGraph.AddVertex('A'), False)

        singleNodeGraph = SimpleGraph(1)

        self.assertEqual(singleNodeGraph.AddVertex('A'), 0)
        self.assertEqual(singleNodeGraph.AddVertex('B'), False)

    def testAddVertexRelations(self):
        graph = SimpleGraph(3)

        graph.AddVertex('A')
        graph.AddVertex('B')
        cIndex = graph.AddVertex('C')

        cMatrixRowRelations = graph.m_adjacency[cIndex]

        self.assertEqual(1 in cMatrixRowRelations, False)
        self.assertEqual(graph.m_adjacency[0][cIndex], 0)
        self.assertEqual(graph.m_adjacency[1][cIndex], 0)

    def testAddEdge(self):
        graph = SimpleGraph(3)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        graph.AddVertex('C')

        self.assertEqual(graph.m_adjacency[aIndex][bIndex], 0)
        self.assertEqual(graph.m_adjacency[bIndex][aIndex], 0)

        graph.AddEdge(aIndex, bIndex)
        self.assertEqual(graph.m_adjacency[aIndex][bIndex], 1)
        self.assertEqual(graph.m_adjacency[bIndex][aIndex], 1)

    def testRemoveEdge(self):
        graph = SimpleGraph(3)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        graph.AddVertex('C')

        graph.AddEdge(aIndex, bIndex)

        self.assertEqual(graph.m_adjacency[aIndex][bIndex], 1)
        self.assertEqual(graph.m_adjacency[bIndex][aIndex], 1)

        graph.RemoveEdge(aIndex, bIndex)

        self.assertEqual(graph.m_adjacency[aIndex][bIndex], 0)
        self.assertEqual(graph.m_adjacency[bIndex][aIndex], 0)

    def testIsEdge(self):
        graph = SimpleGraph(3)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')

        graph.AddEdge(aIndex, bIndex)

        self.assertEqual(graph.IsEdge(aIndex, bIndex), True)
        self.assertEqual(graph.IsEdge(aIndex, cIndex), False)
        self.assertEqual(graph.IsEdge(bIndex, cIndex), False)

    def testDeleteEdge(self):
        graph = SimpleGraph(3)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')

        graph.AddEdge(aIndex, bIndex)
        graph.AddEdge(aIndex, cIndex)

        graph.RemoveVertex(aIndex)

        self.assertEqual(graph.vertex[aIndex], None)
        self.assertEqual(graph.IsEdge(aIndex, bIndex), False)
        self.assertEqual(graph.IsEdge(aIndex, cIndex), False)

    def testDeleteAndAppendOrder(self):
        graph = SimpleGraph(3)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')

        self.assertEqual(len(graph.vertex), graph.max_vertex)

        graph.RemoveVertex(aIndex)

        self.assertEqual(graph.vertex[0], None)
        self.assertEqual(graph.max_vertex, len(graph.vertex))


if __name__ == "__main__":
    unittest.main()
