import sys
sys.path.append("..")
from chapter10.map_base import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""
    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # the scale constant, a, in MAD
        self._shift = randrange(p)  # the shift constant, b, in MAD

    def _hash_function(self, k):
        """Compute hash based on index using the MAD method."""
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)  # maintains self._n
        if self._n > len(self._table) // 2:  # resize if needed to keep laod factor <= 0.5
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        """Resize bucket array to capacity c."""
        old = list(self.items())
        self._table = c * [None]
        self._n = 0  # reset
        for (k, v) in old:  # re-insert old k, v pair
            self[k] = v
