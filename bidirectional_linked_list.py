class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
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

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        len = 0
        while node != None:
            len = len + 1
            node = node.next
        return len

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                newNode.prev = None
                newNode.next = None
                self.head = newNode
                self.tail = newNode
            else:
                currentTail = self.tail
                newNode.prev = currentTail
                newNode.next = None
                currentTail.next = newNode
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    if node == self.tail and node == self.head:
                        newNode.next = None
                        newNode.prev = self.head
                        self.head.next = newNode
                        self.tail = newNode
                        break;
                    elif node == self.tail and node != self.head:
                        newNode.next = None
                        newNode.prev = self.tail
                        self.tail.next = newNode
                        self.tail = newNode
                        break;
                    else:
                        currentNextNode = node.next
                        currentPrevNode = node.prev
                        newNode.next = currentNextNode
                        newNode.prev = currentPrevNode
                        currentPrevNode.next = newNode
                        currentNextNode.prev = newNode
                        break;
                else:
                    node = node.next



    def add_in_head(self, newNode):
        if self.len() == 0:
            newNode.prev = None
            newNode.tail = None
            self.head = newNode
            self.tail = newNode
        else:
            prevHeadNode = self.head
            newNode.prev = None
            newNode.next = prevHeadNode
            self.head = newNode
            prevHeadNode.prev = newNode