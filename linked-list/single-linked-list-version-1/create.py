

"""
to create single linked list there are three steps
-----------------------------------------------------
1. create head and tail, initialize with null

2. create a blank node and assign a value to it and reference to null

3. link head and tail with these node

"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singlylinkedlist = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlylinkedlist.head = node1
singlylinkedlist.head.next = node2
singlylinkedlist.tail = node2