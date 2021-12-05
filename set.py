from logging import currentframe


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
        self.length = 0
    
    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        if self.length == 0:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return

        if self.length == 1:
            getCompare = self.compare(self.head.value, value)
            newNode = Node(value)
            if (self.__ascending == True and getCompare == 1) or (self.__ascending == False and getCompare == -1):
                currentNode = self.head
                newNode.next = currentNode
                currentNode.prev = newNode
                self.head = newNode
                self.length += 1
                return

            elif (self.__ascending == True and getCompare == -1) or (self.__ascending == False and getCompare == 1):
                currentNode = self.head
                newNode.prev = currentNode
                currentNode.next = newNode
                self.tail = newNode
                self.length += 1
                return


        node = self.head
        
        if self.__ascending == True:
            node = self.head

            while node is not None:
                if self.compare(node.value, value) == 1:
                    newNode = Node(value)
                    previousNode = node.prev
                    if previousNode is None:
                        self.head = newNode
                    else:
                        previousNode.next = newNode
                    newNode.prev = previousNode
                    newNode.next = node
                    node.prev = newNode
                    self.length += 1
                    return

                node = node.next
        
        if self.__ascending == False:
            node = self.head

            while node is not None:
                if self.compare(node.value, value) == -1:
                    newNode = Node(value)
                    previousNode = node.prev
                    if previousNode is None:
                        self.head = newNode
                    else:
                        previousNode.next = newNode
                    newNode.prev = previousNode
                    newNode.next = node
                    node.prev = newNode
                    self.length += 1
                    return
                
                node = node.next
        currentNode = self.tail
        newNode = Node(value)
        self.tail = newNode
        newNode.prev = currentNode
        currentNode.next = newNode
        self.length += 1
        return

    def find(self, val):
        node = self.head

        while node is not None:
            if self.__ascending == True and node.value > val:
                return None
            if self.__ascending == False and node.value < val:
                return None
            if node.value == val:
                return node
            node = node.next
        
        return None

    def delete(self, val):
        len = self.len()
        if len == 0:
            return
        
        node = self.head

        while node is not None:
            nextNode = node.next
            if node.value == val and self.head == node and self.tail == node:
                self.tail = None
                self.head = None
                self.length -= 1
                return
            elif node.value == val and self.head == node and self.tail != node:
                currentNextNode = node.next
                currentNextNode.prev = None
                self.head = currentNextNode
                self.length -= 1
                return
            elif node.value == val and self.head != node and self.tail != node:
                currentPrevNode = node.prev
                currentNextNode = node.next
                currentNextNode.prev = currentPrevNode
                currentPrevNode.next = currentNextNode
                self.length -= 1
                return
            elif node.value == val and self.head != node and self.tail == node:
                currentPrevNode = node.prev
                currentPrevNode.next = None
                self.tail = currentPrevNode
                self.length -= 1
                return
                
            node = nextNode

    def len(self):
        return self.length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class PowerSet(OrderedList):
    def __init__(self):
        super().__init__(self)

    def size(self):
        return self.len()
        # количество элементов в множестве

    def put(self, value):
        item_in_set = self.find(value)
        if item_in_set is not None:
            return
        self.add(value)

    def get(self, value):
        item_in_set = self.find(value)
        if item_in_set is None:
            return False
        return True
        # возвращает True если value имеется в множестве,
        # иначе False

    def remove(self, value):
        item_in_set = self.find(value)
        if item_in_set is None:
            return False
        self.delete(value)
        return True
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        result = PowerSet()
        if set2.size() == 0 or self.size() == 0:
            return result
        
        node = set2.head
        while node is not None:
            current_value = node.value
            if self.get(current_value) == True:
                result.add(current_value)
            node = node.next

        return result
        # пересечение текущего множества и set2 

    def union(self, set2):
        result = PowerSet()
        
        node = self.head
        while node is not None:
            current_value = node.value
            result.add(current_value)
            node = node.next
        
        node = set2.head
        while node is not None:
            current_value = node.value
            result.add(current_value)
            node = node.next

        return result
        # объединение текущего множества и set2

    def difference(self, set2):
        result = PowerSet()

        node = self.head
        while node is not None:
            current_value = node.value
            if set2.get(current_value) == False:
                result.add(current_value)
            node = node.next

        return result

    def issubset(self, set2):
        node = set2.head

        while node is not None:
            current_value = node.value
            if self.get(current_value) == False:
                return False
            node = node.next

        return True