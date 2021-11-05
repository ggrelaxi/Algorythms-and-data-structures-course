class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.count += 1

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        if self.head == None:
            return []

        node = self.head

        if node.value == val:
            result.append(node)

        while node.next:
            nextNode = node.next
            if nextNode.value == val:
                result.append(nextNode)
            node = node.next
        return result

    def delete(self, val, all=False):
        if all == False:
            if self.head == None:
                return
            elif self.head != None and self.head == self.tail:
                self.head = None
                self.tail = None
                self.count = 0
            elif self.head != self.tail:
                node = self.head
                nextNode = node.next

                while nextNode != None:
                    if node.value == val and node == self.head:
                        self.head = nextNode
                        self.count -= 1
                        if node.next == self.tail:
                            self.tail = nextNode
                        return
                    elif nextNode.value == val and node == self.tail:
                        self.tail = node
                        self.count -= 1
                        return
                    elif nextNode.value == val and node != self.tail:
                        node.next = nextNode.next
                        self.count -= 1
                        return
                    node = nextNode
                    nextNode = nextNode.next
                    
        else:
            if self.head == None:
                return

            prevNode = None
            node = self.head

            if node.value == val and node.next == None:
                self.head = None
                self.tail = None
                self.count = 0
            elif node.value == val and node.next == self.tail:
                self.head = node.next
                self.count -= 1
            else:
                while node != None:
                    if node.value == val:
                        if prevNode == None:
                            self.head = node.next
                        else:
                            prevNode.next = node.next
                            
                        if node.next == None:
                            self.tail = prevNode
                    else:
                        prevNode = node
                    node = node.next
                    self.count -= 1
            
    def clean(self):
        self.head = None
        self.tail = None
        self.count = 0

    def len(self):
        return self.count

    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                currentHead = self.head
                newNode.next = currentHead
                self.head = newNode
                
            self.count += 1
        else:
            node = self.head
            while node != None:
                if node == afterNode:
                    if node == self.tail:
                        node.next = newNode
                        self.tail = newNode
                        self.count += 1
                        break
                    else:
                        currentNextNode = node.next
                        node.next = newNode
                        newNode.next = currentNextNode
                        self.count += 1
                        break
                else:
                    node = node.next
                self.count += 1

class Deque:
    def __init__(self):
        self.deque = LinkedList()

    def addFront(self, item):
        self.deque.insert(None, Node(item))

    def addTail(self, item):
        self.deque.add_in_tail(Node(item))

    def removeFront(self):
        if self.size() == 0:
            return None
        headValue = self.deque.head.value
        self.deque.delete(headValue)
        return headValue

    def removeTail(self):
        if self.size() == 0:
            return None
        tailValue = self.deque.tail.value
        print(tailValue, 111111)
        node = self.deque.head

        while node != None:
            if node.next == None:
                self.deque.clean()
                return tailValue
            if node.next == self.deque.tail:
                node.next = None
                self.deque.tail = node
                self.deque.count -= 1
                return tailValue
            node = node.next

    def size(self):
        return self.deque.count

# 7.1. Сложности методов будут:
# Добавление/удаление в голову - O(1).
# Добавление в хвост O(1)
# Удаление из хвоста O(n). Потому что нам придеться пройти весь список до хвоста

# 7.2

def checkPalindrom(word):
    wordLen = len(word)
    deque = Deque()
    for x in range(0, wordLen, 1):
        deque.addFront(word[x])

    halfPartLength = len(word) // 2

    for x in range(0, halfPartLength):
        if deque.removeFront() != deque.removeTail():
            return False
    
    return True;