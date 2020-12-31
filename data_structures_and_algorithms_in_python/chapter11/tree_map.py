import sys
sys.path.append("..")
from chapter8.linked_binary_tree import LinkedBinaryTree
from chapter10.map_base import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    def _rebalance_insert(self, p):
        """Rebalance the binary tree after insertion."""
        pass

    def _rebalance_delete(self, p):
        """Rebalance the binary tree after deletion."""
        pass

    def _rebalance_access(self, p):
        """Restructure the binary tree to bring frequently accessed nodes closer to the root (splay tree)."""
        pass

    def _relink(self, parent, child, make_left_child):
        """Relink parent nodde with child node (can be None)."""
        if make_left_child:  # make child a left child
            pare._left = child
        else:  # make child a right child
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent."""
        x = p._node
        y = x._parent
        z = y._parent  # x's grandparent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)  # make x a child of z, replacing y
        # now rotate x and y
        if x == y._left:  # if x is y's left child
            self._relink(y, x._right, True)  # x's right child (the middle subtree T2) becomes y's left child
            self._relink(x, y, False)  # y becomes x's right child
        else:  # if x is y's right child
            self._relink(y, x._left, False)  # x's left child (the middle subtree T2) becomes y's right child
            self._relink(x, y, True)  # y becomse x's left child

    def _restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):  # y is z's right child, x is y's right child
            self._rotate(y)  # single rotation of y above z
            return y
        else:
            self._rotate(x)  # double rotation of x above y, then above z
            self._rotate(x)
            return x

    def _subtree_search(self, p, k):
        """Return Postion of p's subtree having key k, or last node searched."""
        if k == p.key():
            return p
        elif k < p.key():  # search in p's left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:  # search in p's right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p  # upon unsuccessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:  # keep going left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p.
        """
        walk = p
        while self.right(p) is not None:  # keep going right
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree."""
        return self._subtree_first_position(self.root() if len(self) > 0 else None)

    def last(self):
        """Return the last Position in the tree."""
        return self._subtree_last_position(self.root() if len(self) > 0 else None)

    def before(self, p):
        """Return the Position of p's predecessor."""
        self._validate(p)  # inherited from LinkedBinaryTree
        if self.left(p):  # rightmost node in p's left subtree
            return self._subtree_last_position(self.left(p))
        else:  # nearest ancestor such that p is in its right subtree
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above  # walk upward
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position of p's successor."""
        self._validate(p)
        if self.right(p):  # leftmost node in p's right subtree
            return self._subtree_first_position(self.right(p))
        else:  # nearest ancestor such that p is in its left subtree
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k or its neighbor."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self):
        """Return (key, value) pair with least key >= k."""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)  # may be p or p's neighbor
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop."""
        if not self.is_empty():
            if start is None:
                p = self.first()  # initialize p
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)  # find p such that p >= start
                while p is not None and (stop is None or p.key() < stop):
                    yield (p.key(), p.value())
                    p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k."""
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError("Key Error " + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))  # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:  # insert k into p's right subtree
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
            self._rebalance_insert(leaf)

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove item at Position p."""
        self._validate(p)
        if self.left(p) and self.right(p):  # p has two children
            # replacement = self._subtree_last_position(self.left(p)) # replace with p's successor
            replacement = self.before(p)
            self._replace(p, replacement.element())  # inherited from LinkedBinaryTree
            p = replacement  # to delete later
        else:  # p has at most one child
            parent = self.parent(p)
            self.delete(p)
            self._rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item with key k."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # call positional delete method
                return
            self._rebalance_acess(p)
        raise KeyError("Key Error: " + repr(k))
