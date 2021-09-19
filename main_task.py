class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

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
        if self.head == None:
            return
        elif self.head != None and self.head.next == None:
            node = self.head
            if node.value == val:
                self.head = None
                self.tail = None
                return
        else:
            node = self.head
            if node.value == val:
                self.head = node.next
            else:
                while node.next != None:
                    nextNode = node.next
                    if nextNode.value == val:
                        node.next = nextNode.next
                        if all == False:
                            break;
                    node = nextNode.next
                
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        if self.head == None:
            return 0
        else:
            node = self.head
            len = 1

            while node.next:
                len += 1
                node = node.next

            return len

    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head == None:
                self.head = newNode
                self.tail = newNode
            else:
                currentHead = self.head
                self.head = newNode
                newNode.next = currentHead
        else:
            node = self.head
            while node.next:
                if node == afterNode:
                    currentNextNode = node.next
                    node.next = newNode
                    newNode.next = currentNextNode
                    break
                else:
                    node = node.next
