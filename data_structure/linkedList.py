class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = Node(-1)
        self.length = 0
        
    def getAtIndex(self, index):
        if index < self.length:
            node = self.head
            for i in range(0, index+1):
                node = node.next
            return node.val
        else:
            return -float("inf") # error value
        
    def addAtHead(self, val):
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp
        self.length += 1
        
    def addAtTail(self, val):
        node = self.head
        for i in range(0, self.length):
            node = node.next
        node.next = Node(val)
        self.length += 1
        
        # head(-1) -> node(0) -> node(val) -> node(1) -> node(2)
        # current length = 3
        # what if we want to add a node at index of 1
        
    def addAtIndex(self, index, val):
        if index <= self.length:
            node = self.head
            for i in range(0, index):
                node = node.next
            temp = node.next
            node.next = Node(val)
            node.next.next = temp
            self.length += 1
        
    def deleteAtIndex(self, index, val):
        if index < self.length:
            node = self.head
            for i in range(0, index):
                node = node.next
            node.next = node.next.next
        self.length -= 1
        
    def printlist(self):
        node = self.head.next
        while node != None:
            print(node.val)
            node = node.next
        
        
        
test = LinkedList()
test.addAtTail(0)
test.addAtHead(1)
test.addAtTail(2)
test.addAtHead(3)
test.addAtHead(4)
test.addAtIndex(1, 10)
test.addAtIndex(0, 50)
test.addAtIndex(8, 60)

test.printlist()
        
        
        
        