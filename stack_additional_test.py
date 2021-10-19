import unittest
from stack_additional import InvertedStack, isCorrectBrackets, postfixCalc

class TestStack(unittest.TestCase):
    def testLen(self):
        s1 = InvertedStack()

        self.assertEqual(s1.size(), 0)

        s1.push(0)

        self.assertEqual(s1.size(), 1)

        s1.push(1)

        self.assertEqual(s1.size(), 2)

        s1.pop()

        self.assertEqual(s1.size(), 1)

        s1.pop()

        self.assertEqual(s1.size(), 0)

        s1.push(0)
        s1.push(1)
        s1.push(2)

        self.assertEqual(s1.size(), 3)

    def testPush(self):
        s2 = InvertedStack()

        self.assertEqual(s2.size(), 0)

        s2.push(0)

        self.assertEqual(s2.size(), 1)
        self.assertEqual(s2.peek(), 0)

        s2.push(1)

        self.assertEqual(s2.size(), 2)
        self.assertEqual(s2.peek(), 1)

    def testPop(self):
        s3 = InvertedStack()

        self.assertEqual(s3.pop(), None)

        s3.push(0)

        self.assertEqual(s3.peek(), 0)
        self.assertEqual(s3.pop(), 0)
        self.assertEqual(s3.size(), 0)

        s3.push(0)
        s3.push(1)

        self.assertEqual(s3.pop(), 1)
        self.assertEqual(s3.size(), 1)
        self.assertEqual(s3.peek(), 0)

    def testPeek(self):
        s4 = InvertedStack()

        self.assertEqual(s4.peek(), None)

        s4.push(0)

        self.assertEqual(s4.peek(), 0)

        s4.push(1)

        self.assertEqual(s4.peek(), 1)

    def testBrackets(self):
        fixture1 = "((()()()()))"
        fixture2 = "(())(()())"
        fixture3 = "())("
        fixture4 = "))(("
        fixture5 = "((())"

        self.assertEqual(isCorrectBrackets(fixture1), True)
        self.assertEqual(isCorrectBrackets(fixture2), True)
        self.assertEqual(isCorrectBrackets(fixture3), False)
        self.assertEqual(isCorrectBrackets(fixture4), False)
        self.assertEqual(isCorrectBrackets(fixture5), False)

    def testPostfixCalc(self):
        fixture = "8 2 + 5 * 9 + ="

        self.assertEqual(postfixCalc(fixture), 59)
if __name__ == "__main__":
    unittest.main()