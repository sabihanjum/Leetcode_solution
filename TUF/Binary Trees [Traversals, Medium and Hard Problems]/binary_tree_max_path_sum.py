"""A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path."""

import math

class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # Initialize the maximum path sum to negative infinity to account for possible negative values in the tree
        ans = -math.inf

        def maxPathSumDownFrom(root: TreeNode | None) -> int:
            """
            Helper function to calculate the maximum path sum starting from the current root.
            The path must include the root's value.

            Returns:
                int: Maximum path sum starting from the current root.
            """
            nonlocal ans
            if not root:
                return 0  # A null node contributes 0 to the path sum

            # Calculate the maximum path sums from the left and right subtrees
            # If a subtree path sum is negative, consider it as 0 (ignore that subtree)
            l = max(0, maxPathSumDownFrom(root.left))
            r = max(0, maxPathSumDownFrom(root.right))

            # Update the global maximum path sum by considering the path passing through the current root
            ans = max(ans, root.val + l + r)

            # Return the maximum path sum starting from the current root, including one of its subtrees
            return root.val + max(l, r)

        # Trigger the helper function starting from the root node
        maxPathSumDownFrom(root)
        return ans