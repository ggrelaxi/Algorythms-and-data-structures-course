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

# Задание 2

class InvertedStack:

    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return self.stack.len()

    def pop(self):
        if (self.size() == 0):
            return None

        firstElementValue = self.stack.head.value
        self.stack.delete(firstElementValue)

        return firstElementValue

    def push(self, value):
        newNode = Node(value)

        if (self.stack.head == None):
            self.stack.head = newNode
            self.stack.tail = newNode
        elif (self.size() == 1):
            currentHead = self.stack.head
            newNode.next = currentHead
            self.stack.head = newNode
            self.stack.tail = currentHead
        else:
            currentHead = self.stack.head
            newNode.next = currentHead
            self.stack.head = newNode

    def peek(self):
        if (self.size() == 0):
            return None
        
        return self.stack.head.value


# Задание 3

# while stack.size() > 0:
#     print(stack.pop())
#     print(stack.pop())

# В случае с четным количеством элементов в стеке, они будут напечатаны с конца к начала.
# В случае с нечетным - они будут напечатаны также, только в конце будет None

# Задание 4

# pop и push имеют оценку O(1)

def isCorrectBrackets(brackets):
    result = InvertedStack()
    temp = []
    size = 0
    if len(brackets) == 0:
        return True
    for i in range(0, len(brackets), 1):
        currentSymbol = brackets[i]

        if currentSymbol == "(":
            result.push(currentSymbol)
            temp.append(currentSymbol)
            size += 1
        else:
            if result.size() == 0:
                return False
            result.pop()
            temp.pop()
            size -= 1
    return result.size() == 0


#Задание 5

def postfixCalc(expession):
    s1 = InvertedStack()
    s2 = InvertedStack()
    operators = ['+', '*', '=']
    formatExpession = expession.split(' ')

    for x in range(len(formatExpession) - 1, -1, -1):
        s1.push(formatExpession[x])

    for i in range(0, len(formatExpession)):
        currentSymbol = s1.pop()
        if currentSymbol in operators:
            if currentSymbol == '=':
                return s2.peek()

            firstOperator = s2.pop()
            secondOperator = s2.pop()

            if currentSymbol == '+':
                s2.push(firstOperator + secondOperator)
            else:
                s2.push(firstOperator * secondOperator)
            
        else:
            s2.push(int(currentSymbol))