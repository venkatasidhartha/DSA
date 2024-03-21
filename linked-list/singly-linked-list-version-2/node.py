
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None # pointer 

new_node = Node(10)
print(new_node) 

"""
the above print statement will print the memory address of the node 
<__main__.Node object at 0x7d19df05bac0> -> like this
"""


"""
Time and Space Complexity is O(1)
"""



"""
This is a small example how to use Node 
How it works 
"""
linkedLIst = [] # inilizing a list 
for i in range(10):
    new_node = Node(i+1) # insering value in Node 
    if i == 0: # only for First Node just appending the Node to list
        linkedLIst.append(new_node)
    else: # From Second Node attaching the Node memory address to first Node next variable to link  
        linkedLIst[i-1].next = new_node # linking the next node to previous node  
        linkedLIst.append(new_node) # appending the node to list 

node = linkedLIst[0] # just giving the Head for the linked list node 
while node:
    print(node.value)
    node = node.next


# print(linkedLIst)


