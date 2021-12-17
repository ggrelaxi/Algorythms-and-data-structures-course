class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        length = 0
        for x in range(0, len(key), 1):
            length += ord(key[x])

        return length % self.size

    def seek_slot(self, key):
        currentIndex = self.hash_fun(key)

        if self.slots[currentIndex] is not None:
            x = currentIndex + 1

            while x != currentIndex:
                if x >= len(self.slots) or x < 0:
                    x = 0
                elif self.slots[x] is None:
                    return x
                elif x == currentIndex - 1:
                    minIndex = self.hits.index(min(self.hits))
                    return minIndex
                else:
                    x += 1
        else:
            return currentIndex

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        if self.is_key(key) == False:
            index = self.seek_slot(key)
        else:
            index = self.slots.index(key)
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = self.hits[index] + 1

    def get(self, key):
        if self.is_key(key) == False:
            return None
        index = self.slots.index(key)
        value = self.values[index]
        self.hits[index] = self.hits[index] + 1
        return value