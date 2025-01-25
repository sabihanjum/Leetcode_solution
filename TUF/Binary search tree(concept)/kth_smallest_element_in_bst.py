"""Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree."""

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """
        Function to find the k-th smallest element in a Binary Search Tree (BST).
    
        Args:
        root: The root node of the BST.
        k: The position of the smallest element to find (1-based index).
    
        Returns:
        The value of the k-th smallest element in the BST.
        """
        # Initialize a stack to simulate the in-order traversal iteratively.
        stack = []

        # Traverse to the leftmost node of the BST.
        # This represents the smallest element in the BST.
        while root:
            stack.append(root)  # Push the current node onto the stack.
            root = root.left    # Move to the left child.

        # Perform in-order traversal to find the k-th smallest element.
        for _ in range(k - 1):  # We need k-1 pops to reach the k-th element.
            root = stack.pop()    # Pop the topmost node (current smallest element).
            root = root.right     # Move to the right child if it exists.
            while root:           # Push all left descendants of the right child onto the stack.
                stack.append(root)
                root = root.left

        # The k-th smallest element will now be at the top of the stack.
        return stack[-1].val
