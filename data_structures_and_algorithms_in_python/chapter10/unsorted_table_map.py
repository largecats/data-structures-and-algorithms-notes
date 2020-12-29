import sys
sys.path.append("..")
from chapter10.map_base import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""
    def __init__(self):
        """Create an empty map."""
        self._table = []  # list of MapBase._Items

    def __getitem__(self, k):
        """Return value associated with key k."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting exiting value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v  # overwrite exiting value
                return  # quit after found
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)  # remove item at index j
                return  # quit
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key
