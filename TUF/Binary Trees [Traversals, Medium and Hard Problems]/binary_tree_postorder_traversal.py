"""Given the root of a binary tree, return the postorder traversal of its nodes' values."""

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        # List to store the result of the traversal
        ans = []

        # Helper function to perform postorder traversal recursively
        def postorder(root: TreeNode | None) -> None:
            # Base case: If the node is None, return
            if not root:
                return

            # First, recursively traverse the left subtree
            postorder(root.left)
            
            # Then, recursively traverse the right subtree
            postorder(root.right)
            
            # Finally, visit the current node (process its value)
            ans.append(root.val)

        # Start the traversal from the root node
        postorder(root)
        
        # Return the result of the traversal
        return ans
