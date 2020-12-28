class CircularLinkedList:
    
    class Node:
        # to avoid auxiliary namespace dictionary
        # because there may be many nodes in a linked list
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
    
    def is_empty(self):
        return self.size == 0
    
    def add_first(self, e):
        new = self.Node(e, self.head)
        self.head = new
        if self.size == 0:
            self.tail = new
        else:
            self.tail.next = new
        self.size += 1
    
    def add_last(self, e):
        new = self.Node(e, self.head)
        if self.size > 0:
            self.tail.next = new
        else:
            self.head = new
        self.tail = new
        self.size += 1