import unittest
from linked_list import Node
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def testAddInTail(self):
        node1 = Node(1)
        node2 = Node(2)

        list = LinkedList()

        list.add_in_tail(node1)

        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.tail.value, 1)
        self.assertEqual(list.head.next, None)

        list.add_in_tail(node2)

        self.assertEqual(list.head.value, 1)
        self.assertEqual(list.tail.value, 2)
        self.assertEqual(list.head.next, node2)

    def testDelete(self):        
        list = LinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        self.assertEqual(list.delete(1), None)

        list.add_in_tail(node1)

        list.delete(1)

        self.assertEqual(list.head, None)

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)

        list.delete(2)

        self.assertEqual(list.head, node1)
        self.assertEqual(list.tail, node3)
        self.assertEqual(list.length, 2)

    def testClean(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        list = LinkedList()

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)

        list.clean()

        self.assertEqual(list.head, None)
        self.assertEqual(list.tail, None)
        self.assertEqual(list.length, 0)

    def testLen(self):
        list = LinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        self.assertEqual(list.len(), 0)

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        self.assertEqual(list.len(), 3)

    def testInsert(self):
        list = LinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(10)
        
        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        
        self.assertEqual(list.head.value, 1)

        list.insert(node2, node4)
        node = list.find(10)
        self.assertEqual(node.value, 10)
        self.assertEqual(node.next, node3)

    def testFindAll(self):      
        list = LinkedList()

        self.assertEqual(list.find_all(2), [])

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(2)

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        list.add_in_tail(node4)

        self.assertEqual(list.find_all(2), [node2, node4])

if __name__ == "__main__":
    unittest.main()