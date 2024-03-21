"""
There are Three Type of insertion in Linked List Memory 

1. At the beginning of the linked list.
2. in the middle of the linked list.
3. at the end of the linked list.

"""


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        """
        This method is use to print the linked list stored value 
        """
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' -> '
            temp_node = temp_node.next
        return result
        """
        Time Complexity: O(N)
        Space Complexity: O(1) 
        """

    def append(self,value):
        """
        This method is to append the value at the end of the linked list and link it with tail  
        """
        new_node = Node(value)
        if self.head == None and self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

        """
        This append method 
        Time Complexity: O(1)
        Space Complexity: O(1)
        """    
    def prepend(self,value):
        """
        This method is to append the value at the first of the linked list and link it with head 
        """
        new_node = Node(value)
        if self.head == None and self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """ 
    def insert(self,index,value):
        """
        this method is use to insert value in specific index 
        """
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        return True
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """ 

    

new_linkedList = LinkedList()
new_linkedList.append(10)
new_linkedList.append(20)
new_linkedList.append(30)
new_linkedList.prepend(1)
new_linkedList.prepend(2)
print(new_linkedList)
new_linkedList.insert(1,100) 
print(new_linkedList)
