import unittest
from weakvertices import SimpleGraph, Vertex


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

    def testBFS(self):
        graph = SimpleGraph(7)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')
        dIndex = graph.AddVertex('D')
        eIndex = graph.AddVertex('E')
        fIndex = graph.AddVertex('F')
        gIndex = graph.AddVertex('G')

        graph.AddEdge(aIndex, bIndex)
        graph.AddEdge(aIndex, cIndex)
        graph.AddEdge(bIndex, dIndex)
        graph.AddEdge(cIndex, dIndex)
        graph.AddEdge(bIndex, eIndex)
        graph.AddEdge(dIndex, eIndex)
        graph.AddEdge(cIndex, fIndex)
        graph.AddEdge(fIndex, gIndex)

        self.assertEqual(graph.BreadthFirstSearch(0, 1), [
            graph.vertex[0], graph.vertex[1]])
        self.assertEqual(graph.BreadthFirstSearch(0, 2), [
            graph.vertex[0], graph.vertex[2]])
        self.assertEqual(graph.BreadthFirstSearch(0, 3), [
            graph.vertex[0], graph.vertex[1], graph.vertex[3]])
        self.assertEqual(graph.BreadthFirstSearch(0, 4), [
            graph.vertex[0], graph.vertex[1], graph.vertex[4]])

        graph.RemoveEdge(eIndex, bIndex)
        graph.RemoveEdge(eIndex, dIndex)

        self.assertEqual(graph.BreadthFirstSearch(0, 4), [])
        self.assertEqual(graph.BreadthFirstSearch(0, 6), [
            graph.vertex[0], graph.vertex[2], graph.vertex[5], graph.vertex[6]])

        graph2 = SimpleGraph(1)
        aIndex = graph2.AddVertex('A')

        self.assertEqual(graph2.BreadthFirstSearch(0, 0), [
            graph2.vertex[0]])

        graph3 = SimpleGraph(3)

        aIndex = graph3.AddVertex('A')
        bIndex = graph3.AddVertex('B')
        cIndex = graph3.AddVertex('C')

        graph3.AddEdge(aIndex, bIndex)
        graph3.AddEdge(bIndex, cIndex)

        self.assertEqual(graph3.BreadthFirstSearch(0, 1), [
            graph3.vertex[0], graph3.vertex[1]])

        self.assertEqual(graph3.BreadthFirstSearch(0, 2), [
            graph3.vertex[0], graph3.vertex[1], graph3.vertex[2]])

        graph4 = SimpleGraph(4)

        aIndex = graph4.AddVertex('A')
        bIndex = graph4.AddVertex('B')
        cIndex = graph4.AddVertex('C')
        dIndex = graph4.AddVertex('D')

        graph4.AddEdge(aIndex, bIndex)
        graph4.AddEdge(aIndex, cIndex)
        graph4.AddEdge(aIndex, dIndex)

        self.assertEqual(graph4.BreadthFirstSearch(0, 1), [
                         graph4.vertex[0], graph4.vertex[1]])

        self.assertEqual(graph4.BreadthFirstSearch(0, 2), [
            graph4.vertex[0], graph4.vertex[2]])
        self.assertEqual(graph4.BreadthFirstSearch(0, 3), [
            graph4.vertex[0], graph4.vertex[3]])

        self.assertEqual(graph4.BreadthFirstSearch(1, 2), [
            graph4.vertex[1], graph4.vertex[0], graph4.vertex[2]])

    def testLinkedEdges(self):
        graph = SimpleGraph(9)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')
        dIndex = graph.AddVertex('D')
        eIndex = graph.AddVertex('E')
        fIndex = graph.AddVertex('F')
        gIndex = graph.AddVertex('G')
        hIndex = graph.AddVertex('H')
        iIndex = graph.AddVertex('I')

        graph.AddEdge(aIndex, bIndex)
        graph.AddEdge(bIndex, cIndex)
        graph.AddEdge(bIndex, dIndex)
        graph.AddEdge(cIndex, dIndex)
        graph.AddEdge(dIndex, eIndex)
        graph.AddEdge(dIndex, fIndex)
        graph.AddEdge(eIndex, gIndex)
        graph.AddEdge(fIndex, gIndex)
        graph.AddEdge(gIndex, hIndex)
        graph.AddEdge(hIndex, iIndex)
        graph.AddEdge(fIndex, iIndex)

    def testWeakVertices(self):
        graph = SimpleGraph(9)

        aIndex = graph.AddVertex('A')
        bIndex = graph.AddVertex('B')
        cIndex = graph.AddVertex('C')
        dIndex = graph.AddVertex('D')
        eIndex = graph.AddVertex('E')
        fIndex = graph.AddVertex('F')
        gIndex = graph.AddVertex('G')
        hIndex = graph.AddVertex('H')
        iIndex = graph.AddVertex('I')

        graph.AddEdge(aIndex, bIndex)
        graph.AddEdge(bIndex, cIndex)
        graph.AddEdge(bIndex, dIndex)
        graph.AddEdge(cIndex, dIndex)
        graph.AddEdge(dIndex, eIndex)
        graph.AddEdge(dIndex, fIndex)
        graph.AddEdge(eIndex, gIndex)
        graph.AddEdge(fIndex, gIndex)
        graph.AddEdge(fIndex, hIndex)
        graph.AddEdge(gIndex, hIndex)
        graph.AddEdge(hIndex, iIndex)
        graph.AddEdge(fIndex, iIndex)

        self.assertEqual(graph.WeakVertices(), [
                         graph.vertex[0], graph.vertex[4]])


if __name__ == "__main__":
    unittest.main()
