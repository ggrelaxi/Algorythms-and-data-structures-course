class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = int('1'+'0'*32, 2)

    def hash1(self, str1):
        result = 0

        for c in str1:
            code = ord(c)
            result = ((result * 17) + code) % self.filter_len
     
        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % self.filter_len

        return result

    def add(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)

        self.set_bit(firstHash)
        self.set_bit(secondHash)

    def is_value(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)
        
        if self.filter & (1 << firstHash) or self.filter & (1 << secondHash):
            return True
        return False

    def set_bit(self, index):
        m = 1 << index
        self.filter = self.filter | m

