import unittest
from dynamic_array import DynArray

class DynamicArrayTest(unittest.TestCase):

    def testDelete(self):
        da = DynArray()

        da.insert(0, 0)
        da.insert(1, 1)
        da.insert(2, 2)

        da.delete(1)

        self.assertEqual(da.__len__(), 2)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 2)
        self.assertEqual(da.__getitem__(1), 2)

        da.delete(0)

        self.assertEqual(da.__len__(), 1)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 1)
        self.assertEqual(da.__getitem__(0), 2)

        da2 = DynArray()

        for x in range(0, 32, 1):
            da2.append(x)

        for x in range(0, 15, 1):
            da2.delete(x)

        self.assertEqual(da2.count, 17)
        self.assertEqual(da2.__len__(), 17)
        self.assertEqual(da2.capacity, 32)

        da2.delete(0)

        self.assertEqual(da2.count, 16)
        self.assertEqual(da2.__len__(), 16)
        self.assertEqual(da2.capacity, 21)

    def testInsert(self):
        da = DynArray()
        
        da.insert(0, 1)
        self.assertEqual(da.__getitem__(0), 1)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 1)

        da.insert(1, 3)

        self.assertEqual(da.__getitem__(1), 3)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 2)

        da.insert(1, 2)

        self.assertEqual(da.__getitem__(1), 2)
        self.assertEqual(da.__getitem__(2), 3)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 3)

        for x in range(3,16,1):
            da.insert(x, x + 1)
            
        self.assertEqual(da.__getitem__(0), 1)
        self.assertEqual(da.__getitem__(15), 16)
        self.assertEqual(da.__len__(), 16)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 16)

        da.insert(0, 99)

        self.assertEqual(da.__getitem__(0), 99)
        self.assertEqual(da.__getitem__(16), 16)
        self.assertEqual(da.__len__(), 17)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)

        with self.assertRaises(Exception) as context:
            da.insert(40, 100)

            self.assertTrue('Index is out of bounds' in context.exception)

        with self.assertRaises(Exception) as context:
            da.insert(-10, 100)

            self.assertTrue('Index is out of bound' in context.exception)
        
if __name__ == "__main__":
    unittest.main()