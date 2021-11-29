import unittest
from native_dictionary import NativeDictionary

class NativeDictionaryTest(unittest.TestCase):
    def test_put(self):
        n = NativeDictionary(20)
        n.put('ключ1', 'значение1')
        hash = n.hash_fun('ключ1')
        self.assertEqual(n.slots[hash], 'ключ1')
        self.assertEqual(n.values[hash], 'значение1')
        
        n.put('ключ2', 'значение2')
        hash2 = n.hash_fun('ключ2')
        self.assertEqual(n.slots[hash2], 'ключ2')
        self.assertEqual(n.values[hash2], 'значение2')

    def test_is_key(self):
        n = NativeDictionary(20)
        n.put('ключ1', 'значение1')
        self.assertEqual(n.is_key('ключ1'), True)

        n.put('ключ2', 'значение2')
        self.assertEqual(n.is_key('ключ2'), True)
        self.assertEqual(n.is_key('ключ3'), False)

    def test_get(self):
        n = NativeDictionary(20)
        n.put('ключ1', 'значение1')
        self.assertEqual(n.get('ключ1'), 'значение1')
        self.assertEqual(n.get('ключ2'), None)
        n.put('ключ2', 'значение2')
        self.assertEqual(n.get('ключ2'), 'значение2')
        n.put('ключ2', 'значение3')
        self.assertEqual(n.get('ключ2'), 'значение3')

if __name__ == "__main__":
    unittest.main()