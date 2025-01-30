"""Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

If Ceil could not be found, return -1."""

class Solution:
    def findCeil(self, root, inp):
        # Initialize the ceil value to -1 (default if no ceil is found)
        ceil = -1
        
        # If the root is None, return -1 as there is no ceil in an empty tree
        if not root:
            return ceil
        
        # Traverse the BST to find the ceil of inp
        while root:
            # If the node's key matches the input, it's the ceil
            if root.key == inp:
                ceil = root.key
                return ceil

            # If the node's key is greater than inp, it could be a potential ceil
            elif root.key > inp:
                ceil = root.key  # Update ceil
                root = root.left  # Move to the left subtree to find a smaller or equal ceil
                
            # If the node's key is smaller than inp, move to the right subtree
            else:
                root = root.right  # A larger value might exist in the right subtree
        
        # Return the found ceil value or -1 if no valid ceil exists
        return ceil
