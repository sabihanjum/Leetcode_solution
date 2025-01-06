"""Given a binary tree, determine if it is 
height-balanced."""

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Determines whether a binary tree is height-balanced.
        
        A binary tree is balanced if for every node:
        - The difference between the heights of its left and right subtrees is at most 1.
        - Both the left and right subtrees are balanced.

        Args:
        root: TreeNode | None - The root of the binary tree.

        Returns:
        bool - True if the tree is balanced, False otherwise.
        """

        # If the root is None (empty tree), it is considered balanced
        if not root:
            return True

        def maxDepth(root: TreeNode | None) -> int:
            """
            Helper function to calculate the maximum depth of a binary tree.

            Args:
            root: TreeNode | None - The root of the binary tree.

            Returns:
            int - The maximum depth of the binary tree.
            """
            # Base case: If the current node is None, depth is 0
            if not root:
                return 0
            # Recursively calculate the depth of the left and right subtrees
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        # Check the height difference between the left and right subtrees
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        is_current_balanced = abs(left_depth - right_depth) <= 1

        # Recursively check if the left and right subtrees are balanced
        return (is_current_balanced and
                self.isBalanced(root.left) and
                self.isBalanced(root.right))
