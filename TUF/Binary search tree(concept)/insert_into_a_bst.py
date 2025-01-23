"""You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them."""

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Inserts a value into a Binary Search Tree (BST) and returns the updated tree.
        
        :param root: The root node of the BST or None if the tree is empty.
        :param val: The value to be inserted into the BST.
        :return: The root node of the updated BST.
        """
        
        # If the tree is empty (base case), create and return a new node with the value.
        if not root:
            return TreeNode(val)
        
        # If the value to be inserted is less than the current node's value,
        # recursively insert the value into the left subtree.
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # Otherwise, insert the value into the right subtree.
            root.right = self.insertIntoBST(root.right, val)
        
        # Return the root node after inserting the new value.
        return root
