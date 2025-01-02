"""Given the root of a binary tree, return the inorder traversal of its nodes' values."""
class Solution:
    # Function to perform an inorder traversal of a binary tree.
    # Inorder traversal visits nodes in the order: left subtree -> root -> right subtree.
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []  # List to store the result of the inorder traversal
        stack = []  # Stack to simulate the recursion stack manually

        # Iterate until there are nodes to process (either in the stack or as the current root)
        while root or stack:
            # Traverse the left subtree
            while root:
                stack.append(root)  # Push the current node onto the stack
                root = root.left  # Move to the left child

            # Backtrack: process the last node from the stack
            root = stack.pop()  # Pop the node from the stack
            ans.append(root.val)  # Add the node's value to the result list

            # Move to the right subtree
            root = root.right

        return ans  # Return the list containing the inorder traversal

