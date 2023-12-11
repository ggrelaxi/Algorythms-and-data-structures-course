import unittest
from dfs import SimpleGraph, Vertex


class SimpleTreeTest(unittest.TestCase):
    def testHaveReference(self):
        graph = SimpleGraph(5)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')
        dIndex = graph.AddVertex('D')
        eIndex = graph.AddVertex('E')

        graph.AddEdge(aIndex, bIndex)
        graph.AddEdge(aIndex, cIndex)
        graph.AddEdge(aIndex, dIndex)
        graph.AddEdge(cIndex, dIndex)
        graph.AddEdge(bIndex, dIndex)
        graph.AddEdge(bIndex, eIndex)
        graph.AddEdge(dIndex, eIndex)

        self.assertEqual(graph.DepthFirstSearch(0, 1), [
                         graph.vertex[0], graph.vertex[1]])
        self.assertEqual(graph.DepthFirstSearch(0, 2), [
                         graph.vertex[0], graph.vertex[2]])
        self.assertEqual(graph.DepthFirstSearch(0, 3), [
                         graph.vertex[0], graph.vertex[3]])
        self.assertEqual(graph.DepthFirstSearch(0, 4), [
                         graph.vertex[0], graph.vertex[1], graph.vertex[4]])

        graph.RemoveEdge(eIndex, bIndex)
        graph.RemoveEdge(eIndex, dIndex)

        self.assertEqual(graph.DepthFirstSearch(0, 4), [])


if __name__ == "__main__":
    unittest.main()
