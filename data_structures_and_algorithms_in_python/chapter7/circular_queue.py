class CircularQueue:
    
    class _Node:
        # to avoid auxiliary namespace dictionary
        # because there may be many nodes in a linked list
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = head._next
        self._size -= 1
        return head._element
    
    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next