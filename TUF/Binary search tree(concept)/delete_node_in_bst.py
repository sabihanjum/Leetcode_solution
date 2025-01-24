"""Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node."""

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        """
        Deletes a node with the given key from the binary search tree (BST) and returns the updated tree.
        
        :param root: The root of the BST or None if the tree is empty.
        :param key: The value of the node to be deleted.
        :return: The root of the updated BST.
        """
        # Base case: If the root is None, the tree is empty or the key is not found.
        if not root:
            return None

        # If the current node's value matches the key to be deleted.
        if root.val == key:
            # Case 1: Node has no left child, replace it with the right child.
            if not root.left:
                return root.right
            # Case 2: Node has no right child, replace it with the left child.
            if not root.right:
                return root.left
            # Case 3: Node has both children.
            # Find the smallest node in the right subtree to replace the current node.
            minNode = self._getMin(root.right)
            # Recursively delete the smallest node from the right subtree.
            root.right = self.deleteNode(root.right, minNode.val)
            # Replace the current node's left and right children with those of the smallest node.
            minNode.left = root.left
            minNode.right = root.right
            # Update the current node to the smallest node.
            root = minNode

        # If the key is greater than the current node's value, search in the right subtree.
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        # If the key is smaller than the current node's value, search in the left subtree.
        else:  # root.val > key
            root.left = self.deleteNode(root.left, key)

        # Return the root of the updated tree.
        return root

    def _getMin(self, node: TreeNode | None) -> TreeNode | None:
        """
        Helper function to find the smallest node in a binary search tree.
        
        :param node: The root of the subtree.
        :return: The node with the smallest value in the subtree.
        """
        # Traverse to the leftmost node, as it has the smallest value in a BST.
        while node.left:
            node = node.left
        return node
