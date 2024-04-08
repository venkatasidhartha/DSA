

class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self,value):
        self.list.append(value)
        return "The element has been inserted"
        """
        Time Complexity : O(n) or O(n)^2
        Space Complexity : O(1)
        """
    
    def pop(self):
        if self.isEmpty():
            return "Empty List"
        return self.list.pop()
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """

    def peek(self):
        if self.isEmpty():
            return "Empty List"
        return self.list[len(self.list)-1]
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """
    def delete(self):
        self.list = None
        """
        Time Complexity : O(1)
        Space Complexity : O(1)
        """

customStack  = Stack()
print(customStack.isEmpty())