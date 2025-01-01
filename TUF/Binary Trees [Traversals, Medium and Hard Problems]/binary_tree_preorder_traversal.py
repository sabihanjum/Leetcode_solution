"""Given the root of a binary tree, return the preorder traversal of its nodes' values."""

class Solution:
    # Function to perform a preorder traversal of a binary tree.
    # Preorder traversal visits nodes in the order: root -> left subtree -> right subtree.
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []  # List to store the result of the preorder traversal

        # Helper function to recursively perform preorder traversal
        def preorder(root: TreeNode | None) -> None:
            if not root:  # Base case: if the node is None, return
                return

            ans.append(root.val)  # Visit the root node and add its value to the result
            preorder(root.left)   # Recursively traverse the left subtree
            preorder(root.right)  # Recursively traverse the right subtree

        preorder(root)  # Initiate the traversal starting from the root node
        return ans      #
