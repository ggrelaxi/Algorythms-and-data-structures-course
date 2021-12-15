class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0] * f_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        result = 0

        for c in str1:
            code = ord(c)
            result = ((result * 17) + code) % self.filter_len

        return result
        # реализация ...

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % self.filter_len

        return result

    def add(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)

        self.filter[firstHash] = 1
        self.filter[secondHash] = 1

    def is_value(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)

        if self.filter[firstHash] == 0 or self.filter[secondHash] == 0:
            return False
        return True