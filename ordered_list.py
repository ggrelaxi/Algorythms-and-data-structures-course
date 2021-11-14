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
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

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
        # автоматическая вставка value 
        # в нужную позицию

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
        if all == False:
            if self.head == self.tail and self.head.value == val:
                self.head = None
                self.tail = None
            elif self.head != self.tail:
                node = self.head
                nextNode = node.next

                while node is not None:
                    if node.value == val and node == self.head:
                        currentNextNode = node.next
                        currentNextNode.prev = None
                        self.head = currentNextNode
                        return
                    elif node.value == val and node == self.tail:
                        currentPrevNode = node.prev
                        currentPrevNode.next = None
                        self.tail = currentPrevNode
                        return
                    elif node.value == val and node != self.tail:
                        currentPrevNode = node.prev
                        currentNextNode = node.next
                        currentNextNode.prev = currentPrevNode
                        currentPrevNode.next = currentNextNode
                        return
                    node = nextNode
                    nextNode = nextNode.next
        else:
            node = self.head

            while node is not None:
                nextNode = node.next
                if node.value == val and self.head == node and self.tail == node:
                    self.tail = None
                    self.head = None
                elif node.value == val and self.head == node and self.tail != node:
                    currentNextNode = node.next
                    currentNextNode.prev = None
                    self.head = currentNextNode
                elif node.value == val and self.head != node and self.tail != node:
                    currentPrevNode = node.prev
                    currentNextNode = node.next
                    currentNextNode.prev = currentPrevNode
                    currentPrevNode.next = currentNextNode
                elif node.value == val and self.head != node and self.tail == node:
                    currentPrevNode = node.prev
                    currentPrevNode.next = None
                    self.tail = currentPrevNode
                node = nextNode

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        fixV1 = v1.strip()
        fixV2 = v2.strip()

        if fixV1 < fixV2:
            return -1
        elif fixV1 == fixV2:
            return 0
        else:
            return 1