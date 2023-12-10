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

        # self.assertEqual(graph.DepthFirstSearch(0, 1), [0, 1])
        # self.assertEqual(graph.DepthFirstSearch(0, 2), [0, 2])
        # self.assertEqual(graph.DepthFirstSearch(0, 3), [0, 3])
        self.assertEqual(graph.DepthFirstSearch(0, 4), [0, 1, 4])


if __name__ == "__main__":
    unittest.main()
