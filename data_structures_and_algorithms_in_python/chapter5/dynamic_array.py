import ctypes

class DynamicArray:
    
    def __init__(self):
        """Create an empty array."""
        self._n = 0 # number of actual elements in the array
        self._capacity = 1 # capacity of the underlying array
        self._A = self._make_array(self._capacity) # the underlying array
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if k < 0 or k >= self._n:
            raise IndexError('Invalid index')
        return self._A[k]
    
    def append(self, obj):
        if self._n == self._capacity: # not enough room
            # expand underlying array
            self._resize(2 * self._capacity)
        self._A[self._n] = obj # add obj to end of array
        self._n += 1 # increment the recorder of number of elements in array
    
    def _resize(self, c):
        """Expand underlying array to capacity c."""
        newArr = self._make_array(c) # make new array
        for i in range(self._n): # copy elements to new array
            newArr[i] = self._A[i]
        self._A = newArr
        self._capacity = c
    
    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()
    
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # assume 0 <= k <= n for simplicity
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1] # shift rightward
        self._A[k] = value # insert value at position k
        self._n += 1 # increment counter