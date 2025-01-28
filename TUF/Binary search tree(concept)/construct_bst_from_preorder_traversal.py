"""Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right."""

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        # Create the root node with the first value in the preorder list.
        root = TreeNode(preorder[0])
        # Initialize a stack to keep track of nodes for constructing the tree.
        stack = [root]

        # Iterate through the rest of the preorder list.
        for i in range(1, len(preorder)):
            # Start with the top of the stack as the potential parent node.
            parent = stack[-1]
            # Create a new TreeNode for the current value in the preorder list.
            child = TreeNode(preorder[i])
            # Find the correct parent for the current node.
            while stack and stack[-1].val < child.val:
                # Pop from the stack until a valid parent is found.
                parent = stack.pop()
            # Link the child node to the parent according to the BST property.
            if parent.val > child.val:
                # If the child's value is smaller, it's a left child.
                parent.left = child
            else:
                # Otherwise, it's a right child.
                parent.right = child
            # Add the child to the stack for further processing.
            stack.append(child)

        # Return the root of the constructed BST.
        return root
