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

        ht2 = HashTable(5, 3)

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
        self.assertEqual(ht2.size, 5)
        self.assertEqual(ht2.hash_fun('строка6'), 1)
        self.assertEqual(ht2.put('строка6'), None)
        self.assertEqual(ht2.size, 5)
    
    def testSeekSlot(self):
        ht = HashTable(5, 3)

        self.assertEqual(ht.seek_slot('строка1'), 1)
        self.assertEqual(ht.put('строка1'), 1)
        self.assertEqual(ht.seek_slot('строка2'), 2)
        self.assertEqual(ht.put('строка2'), 2)
        self.assertEqual(ht.seek_slot('строка3'), 3)
        self.assertEqual(ht.put('строка3'), 3)
        self.assertEqual(ht.seek_slot('строка4'), 4)
        self.assertEqual(ht.put('строка4'), 4)
        self.assertEqual(ht.seek_slot('строка5'), 0)
        self.assertEqual(ht.put('строка5'), 0)
        self.assertEqual(ht.seek_slot('строка6'), None)
        self.assertEqual(ht.put('строка6'), None)       

    def testPut(self):
        ht = HashTable(19, 3)

        self.assertEqual(ht.put('строка1'), 1)

        ht2 = HashTable(5, 3)

        ht2.put('строка1')
        ht2.put('строка2')
        ht2.put('строка3')
        ht2.put('строка4')
        ht2.put('строка5')
        self.assertEqual(ht2.put('строка6'), None)
        self.assertEqual(len(ht2.slots), 5)

        ht3 = HashTable(19, 3)

        length = 0
        for x in range(0, 100, 1):
            string = 'строка' + str(x)
            slot = ht3.put(string)

            if slot is not None:
                length += 1

        self.assertEqual(length, 19)
    def testFind(self):
        ht = HashTable(19, 3)

        ht.put('строка1')

        self.assertEqual(ht.find('строка1'), 1)
        self.assertEqual(ht.find('строка2'), None)

        ht2 = HashTable(19, 3)

        length = 0
        for x in range(0, 100, 1):
            string = 'строка' + str(x)
            slot = ht2.put(string)
            if slot is not None:
                length += 1

        for x in range(20, 100, 1):
            string = 'строка' + str(x)
            self.assertEqual(ht2.find(string), None)

if __name__ == "__main__":
    unittest.main()