import sys
sys.path.append("..")
from chapter7.doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container  # the positional list the node belongs to
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """
            Return True if the two Positions represent the same location.
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def __init__(self):
        super().__init__()

    def _validate(self, p):
        """
        Return the position's node, or raise error if the position is invalid.
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be of type Position')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is deprecated')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        Return the Position before p.
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        Return the Position after p.
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """
        Add element between nodes and return new Position (instead of node as in the base class).
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        """
        Replace the element of the node at Position p with e.
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
