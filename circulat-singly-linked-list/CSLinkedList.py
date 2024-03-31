

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


"""
creating circulat singly linked list with one element
"""
class CSLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1


csll = CSLinkedList(10)
print(csll.head.value)