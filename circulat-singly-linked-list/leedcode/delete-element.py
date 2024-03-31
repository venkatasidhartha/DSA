class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        # TODO
        if self.head == None:
            return None
        
        if self.head.value == value:
            current_node = self.head
            next_node = self.head.next
            self.head = next_node
            self.tail.next = self.head
            self.length-=1
            return current_node
        
        current_node = self.head
        previous_node = self.head
        while current_node:
            if current_node.value == value:
                break
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node.next = None
        if self.tail.value == value:
            self.tail = previous_node
        self.length-=1
        return current_node
        
csll = CSLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.append(40)
csll.append(50)
csll.append(60)
print(csll)
csll.delete_by_value(60)
print(csll)

