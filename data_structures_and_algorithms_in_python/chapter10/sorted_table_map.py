import sys
sys.path.append("..")
from chapter10.map_base import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.
        
        Return high + 1 if there is no such item.
        """
        if high < low:  # no such item found
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid  # exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)  # search in the left of mid
            else:  # k > self._table[mid]._key
                return self._find_index(k, mid + 1, high)  # search in the right of mid

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:  # no exact match was found
            raise KeyError("Key Error: " + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:  # if j is a valid index for item with key k
            self._table[j]._value = v  # reassign value
        else:  # no such item was found
            self._table.insert(j, self._Item(k, v))  # insert new item

    def __delitem__(self, k):
        """Remove item associated with key k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:  # no exact match was found
            raise KeyError("Key Error: " + repr(k))
        self._table.pop(j)  # delete item if exact match was found

    def __iter__(self):
        """Generate keys of the map ordered from min to max."""
        for item in self._table:  # self._table is sorted, so this is O(n)
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from max to min."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key, value) pair with minimum key."""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key, value) pair with maxminum key."""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key, value) pair with least key >= k."""
        j = self._find_index(k, 0, len(self._table) - 1)  # (j-1)'s key < k <= j's key
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)  # we want item with j's key
        else:
            return None

    def find_lt(self, k):
        """Return (key, value) pair with least key < k."""
        j = self._find_index(k, 0, len(self._table) - 1)  # (j-1)'s key < k <= j's key
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)  # we want item with (j-1)'s key
        else:
            return None

    def find_gt(self, k):
        """Return (key, value) pair with least key > k."""
        j = self._find_index(k, 0, len(self._table) - 1)  # (j-1)'s key < k <= j's key < (j+1)'s key
        if j < len(self._table) and self._table[j]._key == k:
            j += 1  # move past the exact match
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)  # we want (j+1)'s key
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop."""
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
            while j < len(self._table) and (stop is None or self._table[j]._key < stop):
                yield (self._table[j]._key, self._table[j]._value)
                j += 1
