import unittest
from cache import NativeDictionary

class CacheTest(unittest.TestCase):
    def testPut(self):
        c = NativeDictionary(5)

        c.put('0', 0)
        c.put('1', 1)
        c.put('2', 2)
        c.put('3', 3)
        c.put('4', 4)

        c.get('0')
        c.get('1')
        c.get('2')
        c.get('3')

        c.put('10', 10)

        self.assertEqual(c.values[2], 10)
        self.assertEqual(c.slots[2], '10')


if __name__ == "__main__":
    unittest.main()