import unittest
from heap import Heap


class GenerateHeapTest(unittest.TestCase):
    def testEmptyHeap(self):
        heap = Heap()

        self.assertEqual(len(heap.HeapArray), 0)
        self.assertEqual(heap.GetMax(), -1)
        self.assertEqual(heap.Size, 0)

    def testHeapSingleNode(self):
        heap = Heap()

        heap.MakeHeap([1], 0)

        self.assertEqual(len(heap.HeapArray), 1)
        self.assertEqual(heap.HeapArray[0], 1)
        self.assertEqual(heap.Size, 1)
        # self.assertEqual(heap.GetMax(), 1)
        # self.assertEqual(heap.Size, 0)

    def testHeapManyNodes(self):
        # [4, 7, 8, 9, 11]
        heap = Heap()

        heap.MakeHeap([4, 7, 8, 9, 11], 2)
        self.assertEqual(len(heap.HeapArray), 7)
        self.assertEqual(heap.Size, 5)

        self.assertSequenceEqual(
            [11, 9, 8, 4, 7, None, None], heap.HeapArray)

    def testGetMax(self):
        heap = Heap()

        heap.MakeHeap([4, 7, 8, 9, 11], 2)
        print(heap.HeapArray)
        lastMax = heap.HeapArray[heap.Size - 1]
        self.assertEqual(lastMax, 7)
        self.assertEqual(heap.GetMax(), 11)
        self.assertEqual(heap.Size, 4)
        self.assertEqual(heap.HeapArray[heap.Size], None)
        self.assertEqual(heap.GetMax(), 9)
        self.assertEqual(heap.Size, 3)
        self.assertEqual(heap.HeapArray[0], 8)
        self.assertEqual(heap.HeapArray[2], 4)
        self.assertEqual(heap.HeapArray[heap.Size], None)

    def testAdd(self):
        heap = Heap()

        heap.MakeHeap([], 1)

        self.assertEqual(heap.MaxSize, 3)
        self.assertEqual(heap.Size, 0)
        self.assertEqual(heap.Add(1), True)
        self.assertEqual(heap.Add(11), True)
        self.assertEqual(heap.Size, 2)
        self.assertEqual(heap.Add(5), True)
        self.assertEqual(heap.Size, 3)
        self.assertEqual(heap.Add(6), False)


if __name__ == "__main__":
    unittest.main()
