import unittest
from dynamic_array import DynArray

class DynamicArrayTest(unittest.TestCase):

    def testDelete(self):
        pass

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
        print(da.__getitem__(0), da.__getitem__(1))
        self.assertEqual(da.__getitem__(1), 2)
        self.assertEqual(da.__getitem__(2), 3)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 3)

        da.insert(3, 4)
        for x in range(3,16,1):
            da.insert(x, x + 1)
        print(da.__len__(), 111111)
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

        self.assertRaises(da.insert(40, 100), IndexError)

        



if __name__ == "__main__":
    unittest.main()