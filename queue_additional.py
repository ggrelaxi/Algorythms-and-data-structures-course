import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > self.capacity:
            raise IndexError('Index is out of bounds')
        elif i == self.capacity and i == self.count:
            self.resize(2 * self.capacity)
            self.append(itm)
        elif i == 0 and i == self.count:
            self.array[i] = itm
            self.count += 1
        elif i <= self.count:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            for x in range(self.count, i, -1):
                self.array[x] = self.array[x-1]
            self.array[i] = itm
            self.count += 1
        else:
            raise IndexError('Index is out of bounds')

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        if i == 0 and self.count == 1:
            newArray = self.make_array(self.capacity)
            self.array = newArray
            self.count = 0
        else:
            newArray = self.make_array(self.capacity)

            for x in range(0, self.count - 1, 1):
                if x < i:
                    newArray[x] = self.array[x]
                else:
                    newArray[x] = self.array[x+1]

            self.array = newArray
            self.count -= 1
            
            if (self.count < (int(self.capacity / 2))) and self.capacity >= 24:
                self.resize(int(self.capacity // 1.5))

            elif (self.count < (int(self.capacity / 2))) and self.capacity < 24:
                self.resize(16)

class Stack:
    def __init__(self):
        self.stack = DynArray();

    def size(self):
        return self.stack.__len__();

    def pop(self):
        if (self.size() == 0):
            return None;

        lastElementIndex = self.stack.count - 1;
        lastElementValue = self.stack[lastElementIndex];
        self.stack.delete(lastElementIndex);
        
        return lastElementValue;

    def push(self, value):
        self.stack.append(value);

    def peek(self):
        if (self.size() == 0):
            return None # если стек пустой

        return self.stack[self.stack.count - 1]

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
        if all == False:
            if self.head == None:
                return
            elif self.head != None and self.head == self.tail:
                self.head = None
                self.tail = None
            elif self.head != self.tail:
                node = self.head
                nextNode = node.next

                while nextNode != None:
                    if node.value == val and node == self.head:
                        self.head = nextNode
                        if node.next == self.tail:
                            self.tail = nextNode
                        return
                    elif nextNode.value == val and node == self.tail:
                        self.tail = node
                        return
                    elif nextNode.value == val and node != self.tail:
                        node.next = nextNode.next
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
            elif node.value == val and node.next == self.tail:
                self.head = node.next
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
            while node != None:
                if node == afterNode:
                    if node == self.tail:
                        node.next = newNode
                        self.tail = newNode
                        break
                    else:
                        currentNextNode = node.next
                        node.next = newNode
                        newNode.next = currentNextNode
                        break
                else:
                    node = node.next

class Queue:
    def __init__(self):
        self.queue = LinkedList()
        pass

    def enqueue(self, item):
        nodeItem = Node(item)
        self.queue.add_in_tail(nodeItem)

    def dequeue(self):
        if self.size() == 0:
            return None
        headValue = self.queue.head.value
        self.queue.delete(headValue)
        
        return headValue

    def size(self):
        return self.queue.len()


# 6.2

# Сложность обеих операций составляет O(1)

# 6.3

def queueRotation(queue, rotateCount):
    if queue.size() == 0:
        return None
    if queue.size() == 1:
        return queue
    
    for x in range(0, rotateCount, 1):
        queue.enqueue(queue.dequeue())

    return queue

class QueueFromStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def size(self):
        return self.stack1.size()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack1.size() == 0:
            return None
        if self.stack1.size() == 1:
            return self.stack1.pop()
        
        for x in range(self.stack1.size(), 1, -1):
            self.stack2.push(self.stack1.pop())

        headItem = self.stack1.pop()

        for y in range(0, self.stack2.size(), 1):
            self.stack1.push(self.stack2.pop())

        return headItem
