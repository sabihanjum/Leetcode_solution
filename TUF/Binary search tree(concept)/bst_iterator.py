"""Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called."""

class BSTIterator:
    def __init__(self, root: 'TreeNode' | None):
        self.index = 0
        self.values = []
        self._inorder(root)

    def next(self) -> int:
        """Returns the next smallest number."""
        val = self.values[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        """Returns whether the next element exists."""
        return self.index < len(self.values)

    def _inorder(self, root: 'TreeNode' | None) -> None:
        """Performs an inorder traversal to store sorted values."""
        if root:
            self._inorder(root.left)
            self.values.append(root.val)
            self._inorder(root.right)
