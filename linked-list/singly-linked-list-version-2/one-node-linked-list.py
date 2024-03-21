

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None # pointer 


# This is one method
class LinkedList:
    def __init__(self,value):
        new_node = Node(value) # Insering the value in node 
        self.head = new_node # assigining the Node to the head 
        self.tail = new_node # assigining the Node to the tail 
        self.length = 1 #with this variable we can get the length of linked list


ll = LinkedList(10)
print(ll.head)
print(ll.tail)
"""
the above head and tail will have same memory space 
because it is refering to same node 
if we change in one place both variable node will affect 

<__main__.Node object at 0x76149435feb0>
<__main__.Node object at 0x76149435feb0>
"""

# this is another method
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0


