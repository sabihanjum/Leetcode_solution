"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Calculates the maximum depth of a binary tree.
        
        Args:
        root: TreeNode | None - The root node of the binary tree.

        Returns:
        int - The maximum depth of the binary tree.
        """

        # If the current node is None, the depth is 0 (base case for recursion)
        if not root:
            return 0

        # Recursively calculate the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum of the two depths, adding 1 for the current level
        return 1 + max(left_depth, right_depth)
