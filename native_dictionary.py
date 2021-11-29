class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        length = 0
        for x in range(0, len(key), 1):
            length += ord(key[x])

        return length % self.size

    def is_key(self, key):
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        get_hash = self.hash_fun(key)
        self.slots[get_hash] = key
        self.values[get_hash] = value

    def get(self, key):
        if self.is_key(key) == None:
            return None
        hash = self.hash_fun(key)
        value = self.values[hash]
        return value