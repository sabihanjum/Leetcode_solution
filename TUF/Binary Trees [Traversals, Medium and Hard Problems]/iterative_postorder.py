"""Given a binary tree. Find the postorder traversal of the tree without using recursion. Return a list containing the postorder traversal of the tree, calculated without using recursion."""

class Solution:
    def postOrder(self, node):
        """
        Performs an iterative postorder traversal of a binary tree.
        
        Postorder traversal order: left -> right -> root.

        Args:
        node: The root node of the binary tree.

        Returns:
        list[int] - A list containing the values of the nodes in postorder traversal.
        """

        arr = []  # List to store the postorder traversal result.
        
        # If the tree is empty, return an empty list.
        if node is None:
            return arr

        stack = [node]  # Initialize a stack with the root node.
        
        # Iterate while there are nodes in the stack.
        while stack:
            temp = stack.pop()  # Pop the top node from the stack.
            arr.append(temp.data)  # Append the current node's data to the result list.

            # Push the left child of the current node to the stack if it exists.
            if temp.left:
                stack.append(temp.left)

            # Push the right child of the current node to the stack if it exists.
            if temp.right:
                stack.append(temp.right)

        # Reverse the result list to convert root -> right -> left order 
        # into the correct postorder traversal order: left -> right -> root.
        arr.reverse()

        return arr
