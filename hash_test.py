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

        ht2 = HashTable(5, 1)

        self.assertEqual(ht2.hash_fun('строка1'), 1)
        ht2.put('строка1')
        self.assertEqual(ht2.hash_fun('строка2'), 2)
        ht2.put('строка2')
        self.assertEqual(ht2.hash_fun('строка3'), 3)
        ht2.put('строка3')
        self.assertEqual(ht2.hash_fun('строка4'), 4)
        ht2.put('строка4')
        self.assertEqual(ht2.hash_fun('строка5'), 0)
        ht2.put('строка5')
        self.assertEqual(ht2.hash_fun('строка6'), 1)
        self.assertEqual(ht2.put('строка6'), None)
    
    def testSeekSlot(self):
        ht = HashTable(19, 3)

        self.assertEqual(ht.seek_slot('строка1'), 1)
        self.assertEqual(ht.put('строка1'), 1)

        self.assertEqual(ht.put('строка1'), 2)

    def testPut(self):
        ht = HashTable(19, 3)

        self.assertEqual(ht.put('строка1'), 1)

        ht2 = HashTable(5, 1)

        ht2.put('строка1')
        ht2.put('строка2')
        ht2.put('строка3')
        ht2.put('строка4')
        ht2.put('строка5')
        self.assertEqual(ht2.put('строка6'), None)
        self.assertEqual(len(ht2.slots), 5)

    def testFind(self):
        ht = HashTable(19, 3)

        ht.put('строка1')

        self.assertEqual(ht.find('строка1'), 1)
        self.assertEqual(ht.find('строка2'), None)

if __name__ == "__main__":
    unittest.main()