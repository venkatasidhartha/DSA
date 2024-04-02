

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.reverse = False
    
    def __str__(self):
        result = ""
        head = self.head
        if self.reverse:
            head = self.tail
        while head:
            result += str(head.value)
            if self.reverse:
                head = head.prev
            else:
                head = head.next
            if self.reverse:
                if head == self.tail:
                    break
            else:
                if head == self.head:
                    break
            result += " -> "
        return result
    
    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = new_node
        self.length+=1
    
    def prepend(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = new_node
            self.tail.next = new_node
        else:
           new_node.prev = self.head.prev
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node
           self.tail.next = new_node

        self.length+=1
        
    def search(self,value):
        if self.head is None:
            return None
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def get(self,index):
        if index > self.length or index <=-1:
            raise Exception("Index out of range")
        if self.head is None:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def set_value(self,index,value):
        if index > self.length or index <=-1:
            raise Exception("Index out of range")
        if self.head is None:
            return None
        current_node = self.get(index)
        current_node.value = value
        return True

    def insert(self,index,value):
        if index <=-1:
            raise Exception("Index out of range")
        if self.head is None:
            return None
        new_node = Node(value)
        
        if index <= self.length:
            current_node = self.get(index)
            new_node.prev = current_node.prev
            current_node.prev = new_node
            new_node.prev.next = new_node
            new_node.next = current_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = new_node
        self.length+=1

    def pop_first(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            head = self.head.next
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = None
            self.head = head
        self.length-=1
    
    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            tail = self.tail.prev
            self.tail.prev.next = self.tail.next
            self.tail.prev = None
            self.tail.next = None
            self.head.prev = tail
            self.tail = None
            self.tail = tail
        self.length-=1
    
    def remove(self,index):
        if index > self.length or index <=-1:
            raise Exception("Index out of range")
        if self.head is None:
            return None
        if index == 0:
            head = self.head.next
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = None
            self.head = head
        elif index+1 == self.length:
            tail = self.tail.prev
            tail.next = self.head
            self.head.prev = tail 
            self.tail = tail
        else:
            current_node = self.get(index)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            current_node.next = None
            current_node.prev = None
        self.length-=1





cdll = CircularDoublyLL()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.prepend(40)
cdll.reverse = True

# print(cdll.set_value(2,200))
cdll.insert(2,50)
cdll.insert(10,60)

# cdll.pop_first()
# cdll.pop()
cdll.remove(5)

print(cdll)