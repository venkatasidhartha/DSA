

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        
        if self.head == None and self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head == None and self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            head = self.head
            new_node.next = head
            self.head = new_node  
            self.tail.next = new_node
        self.length+=1

    def insert(self,value,index):
        head = self.head
        new_node = Node(value)

        if index > self.length:
            raise Exception("Index Out of Range")

        if index == 0 and self.head is not None:
            new_node.next = head
            self.head = new_node
            self.tail.next = new_node
        elif index == 0 and self.head is None:
            new_node.next = head
            self.head = new_node
            self.tail = new_node
        else:
            for _ in range(index-1):
                head = head.next
            temp_node = head.next
            head.next = new_node
            new_node.next = temp_node
        self.length+=1

    def search(self,target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        
        return False
    
    def get(self,index):
        if index > self.length or index <= -1:
            raise Exception("Index Out of Range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self,index,value):
        temp = self.get(index)
        temp.value = value
        
    def pop_first(self):
        if self.head == None:
            return None
        head = self.head
        self.head = head.next
        self.tail.next = self.head
        self.length-=1
        return head.value

    def pop(self):
        if self.head == None:
            return None
        popped_node = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node.value
        
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        temp.next = self.head
        self.tail = temp
        popped_node.next = None
        self.length-=1
        return popped_node.value
    
    def remove(self,index):
        prev_node = self.get(index-1)
        current_node = self.get(index)
        prev_node.next = current_node.next
        current_node.next = None
        self.length-=1
        return current_node.value
    
    def delete_all(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0
        

    def __str__(self):
        head = self.head
        result = ''
        while head:
            result+=str(head.value)
            head = head.next
            if head == self.head:
                break
            result+=" -> "
        return result


csll = CSLinkedList()
csll.append(1)
csll.append(2)
csll.append(3)
csll.prepend(10)
csll.insert(20,0)
print(csll.search(3))
print("get method",csll.get(0).value)
csll.set_value(2,50)
# print(csll.pop_first())
# print(csll.pop_first())
# print(csll.pop())
print(csll.remove(2))
print(csll.remove(3))
print(csll.delete_all())

print(csll)
