

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.reverse = False

    def __str__(self) -> str:
        result = ""
        head = self.head
        if self.reverse == True:
            head = self.tail
        while head:
            result += str(head.value)
            if self.reverse == True:
                head = head.prev
            else:
                head = head.next
            if head:
                result+=" -> "
        return result
        
    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            head = self.head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def insert(self,index,value):
        if index <= -1:
            raise Exception("Index out of range")
        if self.head is None:
            return None
        
        if index > self.length:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value



    def search(self,value):
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
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value
        return True

    def pop_first(self):
        if self.head is None:
            return None
        head = self.head
        if self.head.next == None:
            self.head = None
            self.tail = None
        else:
            head = self.head
            self.head = self.head.next
            self.head.prev = None
            head.next = None
        self.length-=1
        
        return head.value
    
    def pop(self):
        if self.head is None:
            return None
        tail = self.tail
        if self.head.next == None:
            self.head = None
            self.tail = None
        else: 
            previous_node = self.tail.prev
            self.tail = previous_node
            self.tail.next = None
            tail.prev = None
        self.length-=1
        return tail.value
    
    def remove(self,index):
        if self.head is None:
            return None
        current_node = self.head
        if index == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.get(index)
            if current_node == self.tail:
                self.tail = None 
                self.tail = current_node.prev
                self.tail.next = None
            else:
                current_node.next.prev = current_node.prev
                current_node.next.prev.next = current_node.next
                current_node.prev = None
                current_node.next = None
        self.length-=1
        return current_node.value




dll = doublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.prepend(50)
# dll.insert(0,200)
# print(dll.set_value(4,100))
# print(dll.get(1).value)
# print(dll.search(70))
# dll.reverse = True
print(dll)
# dll.pop_first()
print(dll.remove(4))
print(dll)




