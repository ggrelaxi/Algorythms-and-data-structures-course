class PowerSet():
    def __init__(self):
        self.set = list()

    def size(self):
        return len(self.set)
        # количество элементов в множестве

    def put(self, value):
        if value in self.set:
            return
        self.set.append(value)

    def get(self, value):
        if value in self.set:
            return True
        return False
        # возвращает True если value имеется в множестве,
        # иначе False

    def remove(self, value):
        if value in self.set:
            item_index = self.set.index(value)
            del self.set[item_index]
            return True
        return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        result = PowerSet()
        
        if set2.size() == 0 or self.size() == 0:
            return result

        for i in range (0, len(set2.set)):
            current_item = set2.set[i]
            if current_item in self.set:
                result.set.append(current_item)

        return result
        # пересечение текущего множества и set2 

    def union(self, set2):
        sum = self.set + set2.set
        result_set = set(sum)
        result = PowerSet()
        result.set = list(result_set)
        return result
        # объединение текущего множества и set2

    def difference(self, set2):
        result = PowerSet()
        result.set = self.set

        for i in range(0, len(set2.set)):
            current_item = set2.set[i]
            if current_item in result.set:
                item_index = result.set.index(current_item)
                del result.set[item_index]

        return result

    def issubset(self, set2):
        result = list(self.set)

        for i in range(0, len(set2.set)):
            current_item = set2.set[i]
            if current_item not in result:
                return False
        return True