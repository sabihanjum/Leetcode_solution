"""You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure."""

class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Recovers a BST where two nodes have been swapped by mistake.
        The approach uses in-order traversal to identify the misplaced nodes.
        """

        # Helper function to swap the values of two tree nodes
        def swap(x: TreeNode | None, y: TreeNode | None) -> None:
            temp = x.val
            x.val = y.val
            y.val = temp

        # In-order traversal to find the misplaced nodes
        def inorder(root: TreeNode | None) -> None:
            if not root:
                return

            inorder(root.left)  # Traverse the left subtree

            # Identify misplaced nodes
            if self.pred and root.val < self.pred.val:
                self.y = root  # The second misplaced node
                if not self.x:
                    self.x = self.pred  # The first misplaced node
                else:
                    return  # Exit early after finding both nodes

            self.pred = root  # Update previous node pointer

            inorder(root.right)  # Traverse the right subtree

        # Initialize variables to track misplaced nodes
        self.pred = None  # Previous node during in-order traversal
        self.x = None  # First wrong node
        self.y = None  # Second wrong node

        # Perform in-order traversal to identify the swapped nodes
        inorder(root)

        # Swap the values of the misplaced nodes to correct the BST
        swap(self.x, self.y)
