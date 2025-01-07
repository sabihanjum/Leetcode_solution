"""Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them."""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        # Initialize the answer to store the maximum diameter encountered
        ans = 0

        # Helper function to calculate the maximum depth of the binary tree
        def maxDepth(root: TreeNode | None) -> int:
            nonlocal ans  # To modify the outer variable 'ans' inside this function
            if not root:
                # Base case: if the node is None, its depth is 0
                return 0

            # Recursively calculate the maximum depth of the left subtree
            l = maxDepth(root.left)
            # Recursively calculate the maximum depth of the right subtree
            r = maxDepth(root.right)
            # Update the answer with the maximum diameter found so far
            ans = max(ans, l + r)  # Diameter is the sum of left and right depths
            # Return the depth of the current subtree
            return 1 + max(l, r)

        # Call the helper function to compute the depths and update the diameter
        maxDepth(root)
        return ans  # Return the maximum diameter found
