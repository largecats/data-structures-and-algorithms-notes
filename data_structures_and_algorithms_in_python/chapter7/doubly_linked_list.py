class DoublyLinkedList:
    class Node:
        
        __slots__ = 'element', 'prev', 'next'
        
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        new = self.Node(e, predecessor, successor)
        predecessor.next = new
        successor.prev = new
        self.size += 1
        return new

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element
    
    def add_last(self, e):
        self.insert_between(e, self.trailer.prev, self.trailer)
    
    def traverse(self):
        curr = self.header.next
        while curr.next is not None:
            print(curr.element)
            curr = curr.next