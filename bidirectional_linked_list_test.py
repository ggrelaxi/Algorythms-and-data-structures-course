from os import link
import unittest
from bidirectional_linked_list import Node
from bidirectional_linked_list import LinkedList2

class LinkedListTest(unittest.TestCase):
    def testFind(self):
        linkedList = LinkedList2()

        self.assertEqual(linkedList.find(1), None)

        node1 = Node(1)

        linkedList.add_in_tail(node1)

        self.assertEqual(linkedList.find(1), node1)
        self.assertEqual(linkedList.find(2), None)

        node2 = Node(1)

        linkedList.add_in_tail(node2)

        self.assertEqual(linkedList.find(1), node1)

    def testFindAll(self):
        linkedList = LinkedList2()

        self.assertEqual(linkedList.find_all(1), [])

        node1 = Node(1)
        node2 = Node(2)

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)

        self.assertEqual(linkedList.find_all(1), [node1])
        
        node3 = Node(1)

        linkedList.add_in_tail(node3)

        self.assertEqual(linkedList.find_all(1), [node1, node3])

    def testDeleteSingle(self):
        linkedList = LinkedList2()

        linkedList.delete(1)
        self.assertEqual(linkedList.head, None)
        self.assertEqual(linkedList.tail, None)
        linkedList.delete(1, True)
        self.assertEqual(linkedList.head, None)
        self.assertEqual(linkedList.tail, None)

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(3)
        node5 = Node(3)
        node6 = Node(4)

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node3)

        linkedList.delete(2, False)

        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(linkedList.tail, node3)
        self.assertEqual(node3.next, None)
        self.assertEqual(node3.prev, node1)
        self.assertEqual(linkedList.tail.next, None)
        self.assertEqual(linkedList.tail.prev, node1)

        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node6)

        linkedList.delete(3, False)

        self.assertEqual(linkedList.len(), 3)
        self.assertEqual(linkedList.tail, node6)
        self.assertEqual(node6.next, None)
        self.assertEqual(node6.prev, node4)
        self.assertEqual(node4.next, node6)
        self.assertEqual(node4.prev, node1)
        self.assertEqual(linkedList.tail.next, None)
        self.assertEqual(linkedList.tail.prev, node4)

        linkedList.clean()

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node3)

        linkedList.delete(3, False)

        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(node2.next, None)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(linkedList.tail, node2)
        self.assertEqual(linkedList.tail.next, None)
        self.assertEqual(linkedList.tail.prev, node1)

        linkedList.clean()

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)
        linkedList.add_in_tail(node6)

        linkedList.delete(3, False)

        self.assertEqual(linkedList.len(), 5)
        self.assertEqual(node2.next, node4)
        self.assertEqual(node4.prev, node2)

        linkedList.clean()

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)
        linkedList.add_in_tail(node6)

        linkedList.delete(3, True)

        self.assertEqual(linkedList.len(), 3)
        self.assertEqual(node2.next, node6)
        self.assertEqual(node6.prev, node2)

        linkedList.clean()

        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)
        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node6)

        linkedList.delete(3, False)

        self.assertEqual(linkedList.len(), 5)
        self.assertEqual(node4.prev, None)
        self.assertEqual(node4.next, node5)
        self.assertEqual(linkedList.head, node4)
        self.assertEqual(linkedList.head.prev, None)
        self.assertEqual(linkedList.head.next, node5)

        linkedList.clean()

        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)
        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node6)

        linkedList.delete(3, True)

        self.assertEqual(linkedList.len(), 3)
        self.assertEqual(node1.prev, None)
        self.assertEqual(node1.next, node2)
        self.assertEqual(linkedList.head.prev, None)
        self.assertEqual(linkedList.head.next, node2)

        linkedList.clean()

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node6)
        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)

        linkedList.delete(3, True)

        self.assertEqual(linkedList.len(), 3)
        self.assertEqual(node6.next, None)
        self.assertEqual(node6.prev, node2)
        self.assertEqual(linkedList.tail.next, None)
        self.assertEqual(linkedList.tail.prev, node2)
        self.assertEqual(linkedList.tail, node6)

    def testLen(self):
        linkedList = LinkedList2()

        self.assertEqual(linkedList.len(), 0)

        node1 = Node(1)
        linkedList.add_in_tail(node1)

        self.assertEqual(linkedList.len(), 1)

        node2 = Node(2)
        linkedList.add_in_tail(node2)

        self.assertEqual(linkedList.len(), 2)

    def testClean(self):
        linkedList = LinkedList2()

        linkedList.clean()

        self.assertEqual(linkedList.len(), 0)
        self.assertEqual(linkedList.head, None)
        self.assertEqual(linkedList.tail, None)

        node1 = Node(1)
        node2 = Node(2)

        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)

        linkedList.clean()

        self.assertEqual(linkedList.len(), 0)
        self.assertEqual(linkedList.head, None)
        self.assertEqual(linkedList.tail, None)

    def testAddInTail(self):
        linkedList = LinkedList2()

        node1 = Node(1)
        node2 = Node(2)

        linkedList.add_in_head(node1)

        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node1)

        linkedList.add_in_head(node2)

        self.assertEqual(linkedList.head, node2)
        self.assertEqual(linkedList.tail, node1)

    def testAddInHead(self):
        linkedList = LinkedList2()

        node1 = Node(1)
        node2 = Node(2)

        linkedList.add_in_head(node1)

        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node1)
        self.assertEqual(node1.prev, None)
        self.assertEqual(node1.next, None)

        linkedList.add_in_head(node2)

        self.assertEqual(linkedList.head, node2)
        self.assertEqual(node2.prev, None)
        self.assertEqual(node2.next, node1)
        self.assertEqual(linkedList.head.next, node1)
        self.assertEqual(linkedList.head.prev, None)

        node3 = Node(3)

        linkedList.add_in_head(node3)

        self.assertEqual(linkedList.head, node3)
        self.assertEqual(linkedList.tail, node1)
        self.assertEqual(linkedList.head.next, node2)
        self.assertEqual(linkedList.head.prev, None)
        self.assertEqual(linkedList.tail.next, None)
        self.assertEqual(linkedList.tail.prev, node2)

    def testInsert(self):
        linkedList = LinkedList2();

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        linkedList.insert(None, node1)

        self.assertEqual(linkedList.len(), 1)
        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node1)
        self.assertEqual(node1.next, None)
        self.assertEqual(node1.prev, None)

        linkedList.add_in_tail(node2)

        linkedList.insert(None, node3)

        self.assertEqual(linkedList.len(), 3)
        self.assertEqual(linkedList.find(3), node3)
        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node3)
        self.assertEqual(node1.prev, None)
        self.assertEqual(node1.next, node2)
        self.assertEqual(node3.next, None)
        self.assertEqual(node3.prev, node2)

        linkedList.insert(node3, node4);

        self.assertEqual(linkedList.len(), 4)
        self.assertEqual(linkedList.find(4), node4)
        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node4)
        self.assertEqual(node3.prev, node2)
        self.assertEqual(node3.next, node4)
        self.assertEqual(node4.next, None)
        self.assertEqual(node4.prev, node3)

        linkedList.insert(node4, node5)

        self.assertEqual(linkedList.len(), 5)
        self.assertEqual(linkedList.find(5), node5)
        self.assertEqual(linkedList.head, node1)
        self.assertEqual(linkedList.tail, node5)
        self.assertEqual(node5.next, None)
        self.assertEqual(node5.prev, node4)
        self.assertEqual(node4.next, node5)
        self.assertEqual(node4.prev, node3)
        self.assertEqual(node3.next, node4)
        self.assertEqual(node3.prev, node2)


if __name__ == "__main__":
    unittest.main();