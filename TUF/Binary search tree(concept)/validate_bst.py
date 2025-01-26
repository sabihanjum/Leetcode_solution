"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        stack = []  # Stack to simulate the recursion for in-order traversal
        pred = None  # Variable to store the previous node in in-order traversal

        # Iterate until we exhaust both the stack and the tree
        while root or stack:
            # Traverse to the leftmost node
            while root:
                stack.append(root)  # Push current node to the stack
                root = root.left   # Move to the left child
            root = stack.pop()  # Retrieve the top node from the stack
    
            # If the previous node (pred) exists and its value is greater than or
            # equal to the current node's value, the tree is not a valid BST
            if pred and pred.val >= root.val:
                return False

            pred = root  # Update the previous node to the current node
            root = root.right  # Move to the right child

        # If the traversal completes without finding any violations, the tree is a valid BST
        return True
