import sys
sys.path.append("..")
from chapter10.hash_map_base import HashMapBase


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""
    def _bucket_getitem(self, j, k):
        """Get item with key k in bucket j."""
        bucket = self._table[j]
        if bucket is None:  # no match found
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        """Set item with key k to value v in bucket j."""
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # create new bucket at index j
        oldSize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldSize:  # key is new to the table
            self._n += 1

    def _bucket_delitem(self, j, k):
        """Delete item with key k from bucket j."""
        bucket = self._table[j]
        if bucket is None:  # no match found
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]

    def __iter__(self):
        """Return an iteration of the entires (keys) in the map."""
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
