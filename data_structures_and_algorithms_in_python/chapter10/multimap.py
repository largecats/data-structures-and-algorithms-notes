class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""
    _MapType = dict

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()  # create map instance for storage
        self._n = 0

    def __iter__(self):
        """Iterate through all (k, v) pairs in multimap."""
        for k, secondary in self._map.items():
            for v in secondary:  # the value is also a container for the multiple values associated with key k
                yield (k, v)

    def add(self, k, v):
        """Add pair (k, v) to multimap."""
        container = self._map.setdefault(k, [])  # initialize container with [], if needed
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k, v) with key k."""
        secondary = self._map[k]
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]
        self._n -= 1
        return (k, v)

    def find(self, k):
        """Return arbitrary (k, v) pair with given key."""
        secondary = self._map[k]
        return (k, secondary[0])

    def find_all(self, k):
        """Generate iteration of all (k, v) pairs with given key."""
        secondary = self._map.get(k, [])
        for v in secondary:
            yield (k, v)
