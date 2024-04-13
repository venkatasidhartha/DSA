
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(i) for i in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "Inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]
    
    def delete(self):
        self.items = None

customQueue = Queue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)

print(customQueue.dequeue())
print(customQueue)
