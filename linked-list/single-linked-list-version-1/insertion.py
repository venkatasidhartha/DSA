"""
inserting elements in linked list
---------------------------------
1. at the begginning of the linked list.
2. after a node in the middle of linked list.
3. at the end of the linked list.
"""


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        # this code is to print the value
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertSLL(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # inserting element in single linked list on first 
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            # inserting element in single linked list on last
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            # inserting element in single linked list on middle 
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def iterateSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSSL(self,nodeValue):
        if self.head is None:
            print("The SLL does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Value is not present"


singleLinkedList = SLinkedList()
singleLinkedList.insertSLL(1,1)
singleLinkedList.insertSLL(2,1)
singleLinkedList.insertSLL(3,1)
singleLinkedList.insertSLL(4,1)


singleLinkedList.insertSLL(0,0)
singleLinkedList.insertSLL(16,3)
singleLinkedList.iterateSLL()


print(singleLinkedList.searchSSL(16))
# print([node.value for node in singleLinkedList])

