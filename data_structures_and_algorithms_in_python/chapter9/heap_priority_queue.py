import sys
sys.path.append("..")
from chapter9.priority_queue_base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """Priority queue implemented with a binary heap."""
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap elements at indices i and j."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Up-heap bubbling to adjust position of element at index j to maintain heap order."""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at parent position

    def _downheap(self, j):
        """Down-heap bubbling to adjust positgion of element at index j to maintain heap order."""
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # smaller child of left and right
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []  # array-based

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))  # add to the end of array
        self._upheap(len(self._data) - 1)  # upheap bubbling

    def min(self):
        """Return but do not remove (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data[0]  # item with minimum key is at top of the heap
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k, v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)  # downheap bubbling
        return (item._key, item._value)
