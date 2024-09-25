"""
Input: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8, K = 3
Output: 3 → 2 → 1 → 6 → 5 → 4 → 8 → 7
"""


class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self) -> str:
        if self.head is None:
            return "No Data"
        
        head = self.head
        output = ""
        while head:
            if output == "":
                output = str(head.value) 
            else:
                output = output + "->" + str(head.value)  
            head = head.next
        return output
        
    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return "Inserted"

    def reverse_k_group(self,k):
        if self.head is None:
            return "No Data"
        
        prev = None
        current = self.head
        i = 1
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current          
            current = next_node   
            if i == 3:
                break
            i+=1   
            

        self.head = prev            
            
            
            

linkedlist = LinkedList()
for i in range(1,10):
    linkedlist.append(i)

linkedlist.reverse_k_group(3)
print(linkedlist)
