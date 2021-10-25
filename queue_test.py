import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    def testSize(self):
        q1 = Queue()

        self.assertEqual(q1.size(), 0)

        q1.enqueue(1)

        self.assertEqual(q1.size(), 1)

        q1.enqueue(2)

        self.assertEqual(q1.size(), 2)

    def testEnqueue(self):
        q2 = Queue()
        q2.enqueue(1)

        self.assertEqual(q2.size(), 1)
        self.assertEqual(q2.queue.head.value, 1)
        self.assertEqual(q2.queue.tail.value, 1)

        q2.enqueue(2)

        self.assertEqual(q2.size(), 2)
        self.assertEqual(q2.queue.head.value, 1)
        self.assertEqual(q2.queue.tail.value, 2)

    def testDequeue(self):
        q3 = Queue()
        q3.enqueue(1)

        self.assertEqual(q3.dequeue(), 1)
        self.assertEqual(q3.size(), 0)

        q3.enqueue(1)
        q3.enqueue(2)

        self.assertEqual(q3.dequeue(), 1)
        self.assertEqual(q3.size(), 1)


if __name__ == "__main__":
    unittest.main()

