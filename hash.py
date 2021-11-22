class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        length = 0
        for x in range(0, len(value), 1):
            length += ord(value[x])

        return length % self.size

    def seek_slot(self, value):
        currentIndex = self.hash_fun(value)

        if self.slots[currentIndex] is not None:
            x = currentIndex + 1

            while x != currentIndex:
                if x >= len(self.slots) or x < 0:
                    x = 0
                elif self.slots[x] is None:
                    return x
                elif x == currentIndex - 1:
                    return None
                else:
                    x += 1

        return currentIndex

    def put(self, value):
        availableSlot = self.seek_slot(value)

        if availableSlot is not None:
            self.slots[availableSlot] = value
            return availableSlot
        
        return None

    def find(self, value):
        currentIndex = self.hash_fun(value)

        if self.slots[currentIndex] != value:
            x = currentIndex + 1

            while x != currentIndex:
                if x >= len(self.slots) or x < 0:
                    x = 0
                elif self.slots[x] == value:
                    return x
                elif x == currentIndex - 1:
                    return None
                else:
                    x += 1
        
        return currentIndex