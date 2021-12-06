import unittest
from set import PowerSet

class PowerSetTest(unittest.TestCase):
    def testPut(self):
        new_set = PowerSet()
        new_set.put(1)
        new_set.put(1)
        self.assertEqual(new_set.size(), 1)
        new_set.put(1)
        self.assertEqual(new_set.size(), 1)

    def testGet(self):
        new_set = PowerSet()
        self.assertEqual(new_set.get(1), False)
        new_set.put(1)
        self.assertEqual(new_set.get(1), True)

    def testRemove(self):
        new_set = PowerSet()
        self.assertEqual(new_set.remove(1), False)
        new_set.put(1)
        self.assertEqual(new_set.remove(1), True)
        self.assertEqual(new_set.size(), 0)

    def testIntersection(self):
        new_set = PowerSet()
        new_sub_set = PowerSet()

        for i in range(1, 11):
            if i < 4:
                new_sub_set.put(i)
            new_set.put(i)

        result = new_set.intersection(new_sub_set)

        self.assertEqual(result.size(), 3)
        self.assertEqual(result.get(1), True)
        self.assertEqual(result.get(2), True)
        self.assertEqual(result.get(3), True)

        new_sub_set.remove(1)
        new_sub_set.remove(2)
        new_sub_set.remove(3)

        second_result = new_set.intersection(new_sub_set)

        self.assertEqual(second_result.size(), 0)
        self.assertEqual(second_result.get(1), False)
        self.assertEqual(second_result.get(2), False)
        self.assertEqual(second_result.get(3), False)

        new_sub_set.put(11)

        third_result = new_set.intersection(new_sub_set)

        self.assertEqual(third_result.size(), 0)

    def testUnion(self):
        new_set = PowerSet()
        new_sub_set = PowerSet()

        result = new_set.union(new_sub_set)
        self.assertEqual(result.size(), 0)

        new_set.put(1)
        new_set.put(2)

        second_result = new_set.union(new_sub_set)

        self.assertEqual(second_result.size(), 2)
        self.assertEqual(second_result.get(1), True)
        self.assertEqual(second_result.get(2), True)
        self.assertEqual(second_result.get(3), False)

        new_sub_set.put(3)

        third_result = new_set.union(new_sub_set)

        self.assertEqual(third_result.size(), 3)
        self.assertEqual(third_result.get(1), True)
        self.assertEqual(third_result.get(2), True)
        self.assertEqual(third_result.get(3), True)

    def testDifference(self):
        new_set = PowerSet()
        new_sub_set = PowerSet()

        for i in range(1, 11):
            new_set.put(i)
        
        result = new_set.difference(new_sub_set)

        self.assertEqual(result.size(), 10)

        new_sub_set.put(1)
        new_sub_set.put(2)
        new_sub_set.put(3)
        new_sub_set.put(4)
        new_sub_set.put(5)

        second_result = new_set.difference(new_sub_set)

        self.assertEqual(second_result.size(), 5)
        self.assertEqual(second_result.get(6), True)
        self.assertEqual(second_result.get(7), True)
        self.assertEqual(second_result.get(8), True)
        self.assertEqual(second_result.get(9), True)
        self.assertEqual(second_result.get(10), True)

    def testSubSet(self):
        new_set = PowerSet()

        for i in range(1, 11):
            new_set.put(i)

        new_sub_set = PowerSet()

        self.assertEqual(new_set.issubset(new_sub_set), True)

        new_sub_set.put(1)
        new_sub_set.put(2)

        self.assertEqual(new_set.issubset(new_sub_set), True)

        new_sub_set.put(11)

        self.assertEqual(new_set.issubset(new_sub_set), False)
        
if __name__ == "__main__":
    unittest.main()