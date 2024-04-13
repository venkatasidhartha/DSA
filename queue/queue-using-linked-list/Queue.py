

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head == None:
            return None
        
        next = self.head.next
        head = self.head
        self.head = next
        return head
    
    
    def peek(self):
        if self.head == None:
            return None
        
        return self.head
    
    def isEmpty(self):
         if self.head == None:
            return "queue is empty"
        
    def delete(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = ""
        head = self.head
        while head:
            result += str(head.value)
            head = head.next
            if head == None:
                break
            result += " -> "
        return result 
    
customQueue = LinkedList()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.dequeue()
customQueue.enqueue(30)

print(customQueue.peek().value)
print(customQueue)
