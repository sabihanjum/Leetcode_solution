"""Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity."""

class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        # If the root is None, the tree is empty, so return 0.
        if not root:
            return 0

        # Initialize pointers to traverse the left and right edges of the tree.
        left = root
        right = root

        # Variables to store the heights of the leftmost and rightmost paths.
        heightL = 0
        heightR = 0

        # Traverse the leftmost path and calculate its height.
        while left:
            heightL += 1
            left = left.left

        # Traverse the rightmost path and calculate its height.
        while right:
            heightR += 1
            right = right.right

        # If the heights of the leftmost and rightmost paths are equal,
        # it indicates that the tree is a complete binary tree.
        if heightL == heightR:
            # The number of nodes in a complete binary tree is 2^height - 1.
            return pow(2, heightL) - 1

        # If the heights are not equal, recursively count nodes in the left and right subtrees.
        # Add 1 for the current root node.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
