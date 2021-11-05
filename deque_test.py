import unittest
from deque import Deque
from deque_additional import checkPalindrom

class DequeTest(unittest.TestCase):
    def testAddFront(self):
        q1 = Deque()

        self.assertEqual(q1.size(), 0)

        q1.addFront(0)

        self.assertEqual(q1.size(), 1)
        self.assertEqual(q1.deque.head.value, 0)

        q1.addFront(1)
        
        self.assertEqual(q1.size(), 2)
        self.assertEqual(q1.deque.head.value, 1)
        self.assertEqual(q1.deque.head.next.value, 0)

    def testAddTail(self):
        q1 = Deque()

        self.assertEqual(q1.size(), 0)
        self.assertEqual(q1.deque.tail, None)

        q1.addTail(0)

        self.assertEqual(q1.size(), 1)
        self.assertEqual(q1.deque.tail.value, 0)

        q1.addTail(1)

        self.assertEqual(q1.size(), 2)
        self.assertEqual(q1.deque.tail.value, 1)
        self.assertEqual(q1.deque.head.next.value, 1)

    def testRemoveInFront(self):
        q1 = Deque()

        q1.addFront(0)
        q1.addFront(1)
        q1.addFront(2)

        self.assertEqual(q1.removeFront(), 2)
        self.assertEqual(q1.size(), 2)
        self.assertEqual(q1.removeFront(), 1)
        self.assertEqual(q1.size(), 1)

    def testRemoveInTail(self):
        q1 = Deque()

        q1.addTail(0)
        q1.addTail(1)
        q1.addTail(2)

        self.assertEqual(q1.removeTail(), 2)
        self.assertEqual(q1.size(), 2)
        self.assertEqual(q1.removeTail(), 1)
        self.assertEqual(q1.size(), 1)

    def testPalindrom(self):
        word1 = 'казак'
        word2 = 'потоп'
        word3 = 'строка'

        self.assertEqual(checkPalindrom(word1), True)
        self.assertEqual(checkPalindrom(word2), True)
        self.assertEqual(checkPalindrom(word3), False)

if __name__ == "__main__":
    unittest.main()