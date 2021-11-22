import unittest
from hash import HashTable

class HashTest(unittest.TestCase):
    def testHashFunc(self):
        ht = HashTable(19, 3)

        hash1 = ht.hash_fun('строка1')

        self.assertGreaterEqual(hash1, -1)
        self.assertLessEqual(hash1, ht.size)

        hash2 = ht.hash_fun('Строка2')

        self.assertGreaterEqual(hash2, -1)
        self.assertLessEqual(hash2, ht.size)
    
    def testSeekSlot(self):
        ht = HashTable(19, 3)

        self.assertEqual(ht.seek_slot('строка1'), 1)
        self.assertEqual(ht.put('строка1'), 1)

        self.assertEqual(ht.put('строка1'), 2)

    def testPut(self):
        ht = HashTable(19, 3)

        self.assertEqual(ht.put('строка1'), 1)

    def testFind(self):
        ht = HashTable(19, 3)

        ht.put('строка1')

        self.assertEqual(ht.find('строка1'), 1)
        self.assertEqual(ht.find('строка2'), None)

if __name__ == "__main__":
    unittest.main()