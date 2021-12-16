class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0] * f_len
        self.bit = '0' * f_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        result = 0

        for c in str1:
            code = ord(c)
            result = ((result * 17) + code) % self.filter_len
     
        mask = ''
        
        for i in range(0, self.filter_len):
            if (i == result):
                mask += '1'
            mask += '0'

        return mask

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result = (result * 223 + code) % self.filter_len

        mask = ''

        for i in range(0, self.filter_len):
            if (i == result):
                mask += '1'
            mask += '0'
        return mask

    def add(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)

        result = ''

        for i in range(0, self.filter_len):
            current_first = int(firstHash[i])
            current_second = int(secondHash[i])
            current_filter = int(self.filter[i])

            temp = current_first or current_filter
            temp = temp or current_second
            result += str(temp)    

        self.filter = result

    def is_value(self, str1):
        firstHash = self.hash1(str1)
        secondHash = self.hash2(str1)

        if self.filter[firstHash.index('1')] == 0 or self.filter[secondHash.index('1')] == 0:
            return False
        return True
