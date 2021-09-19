import unittest
from linked_list import Node
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    def testDelete(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        
        list = LinkedList()

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

    def testLen(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)

        list = LinkedList()

        self.assertEqual(list.len(), 0)

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        self.assertEqual(list.len(), 3)

    def testInsert(self):
        list = LinkedList()
        list.insert(None, Node(10))

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        
        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        
        self.assertEqual(list.head.value, 10)

        node4 = Node(15)
        list.insert(node2, node4)
        
        self.assertEqual(list.find(15), node4)

    def testFindAll(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(2)
        
        list = LinkedList()

        self.assertEqual(list.find_all(2), [])

        list.add_in_tail(node1)
        list.add_in_tail(node2)
        list.add_in_tail(node3)
        list.add_in_tail(node4)

        self.assertEqual(list.find_all(2), [node2, node4])
if __name__ == "__main__":
    unittest.main()


