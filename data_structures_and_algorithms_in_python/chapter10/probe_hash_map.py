import sys
sys.path.append("..")
from chapter10.hash_map_base import HashMapBase


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision reolution."""
    _AVAIL = object()  # sentinel marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in at 'bucket' starting at index j.
        
        If match is found, return (True, index).
        Else, return (False, index for first available slot).
        """
        firstAvail = None
        while True:
            if self._is_available(j):  # found a true empty slot
                if firstAvail is None:  # skip over locations marked with previous deletions
                    firstAvail = j  # mark this as first available slot
                if self._table[j] is None:  # this is a true empty slot that is not a previous deletion, so search failed
                    return (False, firstAvail)
            elif k == self._table[j]._key:  # found key k
                return (True, j)
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        """Find item with key k at 'bucket' starting at index j."""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def __bucket_setitem(self, j, k, v):
        """Set item with key k to value v at 'bucket' starting at index j."""
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        """Delete item with key k at 'bucket' starting at index j."""
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        self._table[s] = ProbeHashMap._AVAIL  # mark position as deleted

    def __iter__(self):
        """Return an iteration of all entries in the map."""
        for j in range(len(self._table)):
            if not self._is_available(j):  # if occupied (i.e., not empty and not deprecated)
                yield self._table[j]._key
