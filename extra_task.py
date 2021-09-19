def sumOfLinkedLists (list1, list2):
    if list1.len() != list2.len():
        return
    else:
        result = []
        firstNode = list1.head
        secondNode = list2.head

        while firstNode != None:
            result.append(firstNode.value + secondNode.value)
            firstNode = firstNode.next
            secondNode = secondNode.next

    return result
