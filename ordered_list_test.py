import unittest
from ordered_list import OrderedList

class OrderedListTest(unittest.TestCase):
    def testLen(self):
        pass

    def testAdd(self):
        list = OrderedList(True)

        list.add(1)

        self.assertEqual(list.length, 1)
        list.add(2)

        self.assertEqual(list.length, 2)
        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.tail.value, 2)

        list.add(5)

        self.assertEqual(list.length, 3)
        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.tail.value, 5)

        list.add(4)

        self.assertEqual(list.length, 4)
        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.tail.value, 5)
        self.assertEqual(list.tail.prev.value, 4)

        list2 = OrderedList(False)

        list2.add(5)

        self.assertEqual(list2.length, 1)
        self.assertEqual(list2.head.value, 5)
        self.assertEqual(list2.tail.value, 5)

        list2.add(1)

        self.assertEqual(list2.length, 2)
        self.assertEqual(list2.head.value, 5)
        self.assertEqual(list2.tail.value, 1)

        list2.add(3)

        self.assertEqual(list2.length, 3)
        self.assertEqual(list2.head.value, 5)
        self.assertEqual(list2.tail.value, 1)
        self.assertEqual(list2.head.next.value, 3)
        self.assertEqual(list2.tail.prev.value, 3)

        list2.delete(3)

        self.assertEqual(list2.length, 2)
        self.assertEqual(list2.head.value, 5)
        self.assertEqual(list2.tail.value, 1)
        self.assertEqual(list2.head.next.value, 1)
        self.assertEqual(list2.tail.prev.value, 5)
        
if __name__ == "__main__":
    unittest.main()