"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """Determines if two binary trees, p and q, are identical in structure and values.
    Args:
        p (TreeNode | None): The root node of the first tree.
        q (TreeNode | None): The root node of the second tree.
        
    Returns:
        bool: True if the trees are identical, False otherwise.
    """
    
        # Base case: If either p or q is None (empty subtree)
        if not p or not q:
        # Both must be None for the trees to be the same at this point
            return p == q

        # Recursive case: Check current node values and recursively check subtrees
        return (p.val == q.val and  # Check if current node values are the same
            self.isSameTree(p.left, q.left) and  # Recursively check left subtrees
            self.isSameTree(p.right, q.right))  # Recursively check right subtrees
