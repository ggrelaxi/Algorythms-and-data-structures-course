import unittest
from stack import Stack;

class TestStack(unittest.TestCase):
    def testLen(self):
        s1 = Stack()

        self.assertEqual(s1.size(), 0)

        s1.push(0);

        self.assertEqual(s1.size(), 1)

    def testPush(self):
        s2 = Stack()

        s2.push(0)

        self.assertEqual(s2.size(), 1)
        self.assertEqual(s2.stack.__getitem__(0), 0)

    def testPop(self):
        s3 = Stack()

        self.assertEqual(s3.pop(), None)

        s3.push(0)

        self.assertEqual(s3.pop(), 0)
        self.assertEqual(s3.size(), 0)

    def testPeek(self):
        s4 = Stack()

        self.assertEqual(s4.peek(), None)

        s4.push(0)

        self.assertEqual(s4.peek(), 0)

if __name__ == "__main__":
    unittest.main()