class ArrayQueue:
    DEFAULT_CAPACITY = 5
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        dequeued = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return dequeued
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        enqueueIndex = (self._front + self._size) % len(self._data)
        self._data[enqueueIndex] = e
        self._size += 1
        
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        
    def print(self):
        l = [None] * self._size
        pointer = self._front
        counter = 0
        while self._data[pointer]:
            l[counter] = self._data[pointer]
            counter += 1
            pointer = (pointer + 1) % len(self._data)
        print(l)