class LinkedList:
    
    class Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def add_first(self, e):
        new = self.Node(e, self.head)
        self.head = new
        self.size += 1
    
    def add_last(self, e):
        new = self.Node(e, None)
        if self.size == 0:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1
    
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.element)
            curr = curr.next