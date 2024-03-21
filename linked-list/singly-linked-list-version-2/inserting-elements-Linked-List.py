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
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """ 
    def search(self,target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index+=1
        return -1
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """ 
    
    def get(self,index):
        if index == -1:
            return self.tail 
        if index < -1 or index > self.length:
            return None
        current_node = self.head
        for i in range(index+1):
            if i == index:
                return current_node
            current_node = current_node.next
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """ 
    def set_value(self,index,value):
        # we can try like this 
        # current_node = self.head
        # for i in range(index+1):
        #     if i == index:
        #         current_node.value = value
        #         break
        #     current_node = current_node.next

        # or
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False  
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length-=1
        return popped_node
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            self.tail = current_node
            current_node.next = None
        self.length-=1
        return popped_node
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

    def remove(self,index):
        if self.length == 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length-=1
        return popped_node
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        """
        Time Complexity: O(1)
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
# new_linkedList.traverse()
# print(new_linkedList.search(100))
# print(new_linkedList.get(0))
print(new_linkedList.pop_first())
print(new_linkedList)


