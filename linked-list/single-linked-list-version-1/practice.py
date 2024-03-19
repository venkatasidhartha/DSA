

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SSL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,value,location,insertSpecificIndex=0):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == "first":
                newNode.next = self.head
                self.head = newNode
            elif location == "last":
                # newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            elif location == "middle":
                tempNode = self.head
                index = 0
                while index < insertSpecificIndex - 1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode



        
    def get_values(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

ssl = SSL()
ssl.insert(1,"first")
ssl.insert(2,"last")
ssl.insert(3,"last")
ssl.insert(4,"last")
ssl.insert("5","last")

ssl.insert("sidhu","middle",3)





ssl.get_values()



