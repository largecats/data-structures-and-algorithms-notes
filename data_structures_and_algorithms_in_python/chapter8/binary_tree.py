from tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.paarent(p)
        if parent is None:  # p is the root
            return None  # root has no sibiling
        else:
            if p == self.left(parent):  # if p is the left child, returns the right child
                return self.right(parent)
            else:  # vice versa
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            yield from self._subtree_inorder(self.left(p))
        yield p
        if self.right(p) is not None:
            yield from self._subtree_inorder(self.right(p))

    def positions(self):  # overwrite the postorder traveral inherited from (general) Tree
        """Generate an iteration of the tree's positions."""
        return self.inorder()
