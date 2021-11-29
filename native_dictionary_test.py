import unittest
from native_dictionary import NativeDictionary

class NativeDictionaryTest(unittest.TestCase):
    # def test_put(self):
    #     n = NativeDictionary(20)

    #     index = n.seek_slot('ключ1')
    #     n.put('ключ1', 'значение1')
    #     self.assertEqual(n.slots[index], 'ключ1')
    #     self.assertEqual(n.values[index], 'значение1')
        
    #     index2 = n.seek_slot('ключ2')
    #     n.put('ключ2', 'значение2')
    #     self.assertEqual(n.slots[index2], 'ключ2')
    #     self.assertEqual(n.values[index2], 'значение2')

    # def test_is_key(self):
    #     n = NativeDictionary(20)
    #     n.put('ключ1', 'значение1')
    #     self.assertEqual(n.is_key('ключ1'), True)

    #     n.put('ключ2', 'значение2')
    #     self.assertEqual(n.is_key('ключ2'), True)
    #     self.assertEqual(n.is_key('ключ3'), False)

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