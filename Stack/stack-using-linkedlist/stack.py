class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    
    def __str__(self) -> str:
        head = self.head
        result = ""
        while head:
            result += str(head.value)
            head = head.next
            if head == None:
                break
            result += " -> "
        return result


    def push(self,value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def peek(self):
        return self.head

    def pop(self):
        head = self.head 
        next = head.next
        head.next = None 
        self.head = next
        return head

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def delete(self):
        self.head = None



ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
print(ll.pop().next)
print(ll.peek().value)

print(ll)
