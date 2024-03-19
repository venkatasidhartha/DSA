


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None


node1 = Node(1)
node2 = Node(2)

sll = SLL()
sll.head = node1
sll.head.next = node2
sll.tail = node2

node3 = Node(3)
sll.tail.next = node3
sll.tail = node3


for  i in [sll.head.value,sll.head.next.value,sll.tail.value]:
    print(i)
