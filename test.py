class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def get(self,index):
        if index < -1 or index > self.length:
            return None
        head_node = self.head
        for i in range(index+1):
            if i == index:
                return head_node
            head_node = head_node.next
    
    
    def remove(self,index):
        if index >= self.length:
            return None
        if index == 0:
            head = self.head
            next_node = self.head.next
            self.head = next_node
            self.length-=1
            return head
        else:
            previous_node = self.get(index-1)
            pop_node = self.get(index)
            
            previous_node.next = pop_node.next
            pop_node.next = None
            self.length-=1
            return pop_node
        
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev 

    def find_middle(self):
        average = self.length//2
        head = self.head
        for _ in range(average):
            head = head.next
        return head
    
    def remove_duplicates(self):
        head = self.head

        while head:
            current_address = head
            next_address = head.next
            previous_address = head
            while next_address:
                if current_address.value == next_address.value:
                    previous_address.next = next_address.next
                else:
                    previous_address = next_address
                next_address = next_address.next
            head = head.next
           
    # def remove_duplicates(self):
    #     if self.head is None:
    #         return
    #     node_values = set()  # set to store unique node values
    #     current_node = self.head
    #     node_values.add(current_node.value)
    #     while current_node.next:
    #         if current_node.next.value in node_values:  # duplicate found
    #             current_node.next = current_node.next.next
    #             self.length -= 1
    #         else:
    #             node_values.add(current_node.next.value)
    #             current_node = current_node.next
    #     self.tail = current_node
            

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(1)
ll.append(3)




# print(ll.remove(4).value)
# print(ll.reverse())
print(ll)
print(ll.remove_duplicates())
print(ll)


            
            
            