import unittest
from blum import BloomFilter

s1 = '0123456789'
s2 = '1234567890'
s3 = '2345678901'
s4 = '3456789012'
s5 = '4567890123'
s6 = '5678901234'
s7 = '6789012345'
s8 = '7890123456'
s9 = '8901234567'
s10 = '9012345678'

class BloomFilterTest(unittest.TestCase):
    def testAdd(self):
        b = BloomFilter(32)

        hash1_s1 = b.hash1(s1)
        hash1_s2 = b.hash1(s2)
        hash1_s3 = b.hash1(s3)
        hash1_s4 = b.hash1(s4)
        hash1_s5 = b.hash1(s5)
        hash1_s6 = b.hash1(s6)
        hash1_s7 = b.hash1(s7)
        hash1_s8 = b.hash1(s8)
        hash1_s9 = b.hash1(s9)
        hash1_s10 = b.hash1(s10)

        hash2_s1 = b.hash1(s1)
        hash2_s2 = b.hash1(s2)
        hash2_s3 = b.hash1(s3)
        hash2_s4 = b.hash1(s4)
        hash2_s5 = b.hash1(s5)
        hash2_s6 = b.hash1(s6)
        hash2_s7 = b.hash1(s7)
        hash2_s8 = b.hash1(s8)
        hash2_s9 = b.hash1(s9)
        hash2_s10 = b.hash1(s10)

        b.add(s1)
        b.add(s2)
        b.add(s3)
        b.add(s4)
        b.add(s5)
        b.add(s6)
        b.add(s7)
        b.add(s8)
        b.add(s9)
        b.add(s10)

        self.assertEqual(b.filter[hash1_s1.index('1')], '1')
        self.assertEqual(b.filter[hash2_s1.index('1')], '1')

        self.assertEqual(b.filter[hash1_s2.index('1')], '1')
        self.assertEqual(b.filter[hash2_s2.index('1')], '1')

        self.assertEqual(b.filter[hash1_s3.index('1')], '1')
        self.assertEqual(b.filter[hash2_s3.index('1')], '1')

        self.assertEqual(b.filter[hash1_s4.index('1')], '1')
        self.assertEqual(b.filter[hash2_s4.index('1')], '1')

        self.assertEqual(b.filter[hash1_s5.index('1')], '1')
        self.assertEqual(b.filter[hash2_s5.index('1')], '1')

        self.assertEqual(b.filter[hash1_s6.index('1')], '1')
        self.assertEqual(b.filter[hash2_s6.index('1')], '1')

        self.assertEqual(b.filter[hash1_s7.index('1')], '1')
        self.assertEqual(b.filter[hash2_s7.index('1')], '1')

        self.assertEqual(b.filter[hash1_s8.index('1')], '1')
        self.assertEqual(b.filter[hash2_s8.index('1')], '1')

        self.assertEqual(b.filter[hash1_s9.index('1')], '1')
        self.assertEqual(b.filter[hash2_s9.index('1')], '1')

        self.assertEqual(b.filter[hash1_s10.index('1')], '1')
        self.assertEqual(b.filter[hash2_s10.index('1')], '1')

    def testIsValue(self):
        b = BloomFilter(32)

        b.add(s1)
        b.add(s2)
        b.add(s3)
        b.add(s4)
        b.add(s5)
        b.add(s6)
        b.add(s7)
        b.add(s8)
        b.add(s9)
        b.add(s10)

        self.assertEqual(b.is_value(s1), True)
        self.assertEqual(b.is_value(s2), True)
        self.assertEqual(b.is_value(s3), True)
        self.assertEqual(b.is_value(s4), True)
        self.assertEqual(b.is_value(s5), True)
        self.assertEqual(b.is_value(s6), True)
        self.assertEqual(b.is_value(s7), True)
        self.assertEqual(b.is_value(s8), True)
        self.assertEqual(b.is_value(s9), True)
        self.assertEqual(b.is_value(s10), True)

if __name__ == "__main__":
    unittest.main()