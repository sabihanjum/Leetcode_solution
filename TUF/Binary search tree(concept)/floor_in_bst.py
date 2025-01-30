"""You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1."""

class Solution:
    def floor(self, root, x):
        # Initialize the floor value to -1 (default if no floor is found)
        floor = -1
        
        # If the root is None, return -1 as there is no floor in an empty tree
        if not root:
            return floor  # Fixed typo (previously "return ceil")
        
        # Traverse the BST to find the floor of x
        while root:
            # If the node's value matches x, it's the floor
            if root.data == x:
                floor = root.data
                return floor

            # If the node's value is smaller than x, it could be a potential floor
            elif root.data < x:
                floor = root.data  # Update floor
                root = root.right  # Move to the right subtree to find a closer or equal floor
                
            # If the node's value is greater than x, move to the left subtree
            else:
                root = root.left  # A smaller value might exist in the left subtree
        
        # Return the found floor value or -1 if no valid floor exists
        return floor
