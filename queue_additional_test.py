import unittest
from queue_additional import Queue, QueueFromStack, queueRotation

class Queue_Additional(unittest.TestCase):
    def test_rotation(self):
        q1 = Queue()

        rotation1 = queueRotation(q1, 2)

        self.assertEqual(rotation1, None)

        q2 = Queue()
        q2.enqueue(1)

        rotation2 = queueRotation(q2, 3)

        self.assertEqual(rotation2, q2)

        q2.enqueue(2)

        rotation3 = queueRotation(q2, 1)

        self.assertEqual(rotation3.queue.head.value, 2)
        self.assertEqual(rotation3.queue.tail.value, 1)

        q3 = Queue()

        q3.enqueue(1)
        q3.enqueue(2)
        q3.enqueue(3)

        rotation4 = queueRotation(q3, 2)

        self.assertEqual(rotation4.queue.head.value, 3)
        self.assertEqual(rotation4.queue.tail.value, 2)

    def testQueueFromStack(self):
        qs = QueueFromStack()

        self.assertEqual(qs.size(), 0)

        qs.enqueue(1)

        self.assertEqual(qs.size(), 1)
        self.assertEqual(qs.dequeue(), 1)
        self.assertEqual(qs.size(), 0)

        qs.enqueue(1)
        qs.enqueue(2)
        qs.enqueue(3)
        qs.enqueue(4)

        self.assertEqual(qs.size(), 4)
        self.assertEqual(qs.dequeue(), 1)
        self.assertEqual(qs.size(), 3)
        self.assertEqual(qs.stack1.stack[0], 2)
        self.assertEqual(qs.stack1.stack[1], 3)
        self.assertEqual(qs.stack1.stack[2], 4)

if __name__ == "__main__":
    unittest.main()