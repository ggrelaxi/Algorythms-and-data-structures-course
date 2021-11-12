class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = self.tail = item
        else:
            self.tail.next = self.tail = item
        self.length += 1

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
        if self.head.next == None:
            if self.head.value == val:     
                self.head = None
                self.tail = None
                self.length = 0
            return

        node = self.head
        nextNode = node.next

        while nextNode != None:
            if node.value == val and node == self.head:
                self.head = nextNode
                if node.next == self.tail:
                    self.tail = nextNode
                    self.length -= 1
                return
            elif nextNode.value == val and node == self.tail:
                self.tail = node
                self.length -= 1
                return
            elif nextNode.value == val and node != self.tail:
                node.next = nextNode.next
                self.length -= 1
                return
            node = nextNode
            nextNode = nextNode.next

            if all == False:
                break
        # if all == False:
        #     if self.head == None:
        #         return
        #     elif self.head != None and self.head == self.tail:
        #         self.head = None
        #         self.tail = None
        #         self.length = 0
        #     elif self.head != self.tail:
        #         node = self.head
        #         nextNode = node.next

        #         while nextNode != None:
        #             if node.value == val and node == self.head:
        #                 self.head = nextNode
        #                 if node.next == self.tail:
        #                     self.tail = nextNode
        #                 return
        #             elif nextNode.value == val and node == self.tail:
        #                 self.tail = node
        #                 return
        #             elif nextNode.value == val and node != self.tail:
        #                 node.next = nextNode.next
        #                 return
        #             node = nextNode
        #             nextNode = nextNode.next
        # else:
        #     if self.head == None:
        #         return

        #     prevNode = None
        #     node = self.head

        #     if node.value == val and node.next == None:
        #         self.head = None
        #         self.tail = None
        #     elif node.value == val and node.next == self.tail:
        #         self.head = node.next
        #     else:
        #         while node != None:
        #             if node.value == val:
        #                 if prevNode == None:
        #                     self.head = node.next
        #                 else:
        #                     prevNode.next = node.next
                            
        #                 if node.next == None:
        #                     self.tail = prevNode
        #             else:
        #                 prevNode = node
        #             node = node.next
            
    def clean(self):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = self.tail = newNode
            return
        
        currentNode = self.head

        while currentNode != None:
            if currentNode == afterNode:
                if currentNode.next == None:
                    self.tail = newNode
                newNode.next = currentNode.next
                currentNode.next = newNode
                break
            currentNode = currentNode.next


        # if afterNode == None:
        #     if self.head == None:
        #         self.head = newNode
        #         self.tail = newNode
        #     else:
        #         currentHead = self.head
        #         self.head = newNode
        #         newNode.next = currentHead
        #     self.count += 1
        # else:
        #     node = self.head
        #     while node != None:
        #         if node == afterNode:
        #             if node == self.tail:
        #                 node.next = newNode
        #                 self.tail = newNode
        #                 self.count += 1
        #                 break
        #             else:
        #                 currentNextNode = node.next
        #                 node.next = newNode
        #                 newNode.next = currentNextNode
        #                 self.count += 1
        #                 break
        #         else:
        #             node = node.next
        #         self.count += 1
