"""You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null."""

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # Base case: If the current node is None, the value is not found in the BST
        if not root:
            return None

        # If the current node's value matches the target value, return the current node
        if root.val == val:
            return root

        # If the target value is smaller than the current node's value,
        # recursively search the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)

        # If the target value is greater than the current node's value,
        # recursively search the right subtree
        return self.searchBST(root.right, val)
