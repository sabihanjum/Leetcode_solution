"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself."""

import collections

class Codec:
    def serialize(self, root: 'TreeNode') -> str:
        """
        Encodes a binary tree to a single string using level-order traversal.
        
        Args:
            root (TreeNode): The root of the binary tree.
        
        Returns:
            str: A space-separated string representing the serialized tree. 'n' represents null nodes.
        """
        if not root:
            return ''  # Return an empty string if the tree is empty.

        s = ''  # Initialize the result string.
        q = collections.deque([root])  # Use a queue for level-order traversal.

        while q:
            node = q.popleft()  # Dequeue the current node.
            if node:
                s += str(node.val) + ' '  # Append the value of the node to the string.
                q.append(node.left)  # Enqueue the left child (can be None).
                q.append(node.right)  # Enqueue the right child (can be None).
            else:
                s += 'n '  # Append 'n' to represent a null node.

        return s  # Return the serialized string.

    def deserialize(self, data: str) -> 'TreeNode':
        """
        Decodes the serialized string back to a binary tree.
        
        Args:
            data (str): A space-separated string representing the serialized tree.
        
        Returns:
            TreeNode: The root of the deserialized binary tree.
        """
        if not data:
            return None  # Return None if the serialized string is empty.

        vals = data.split()  # Split the string into a list of node values.
        root = TreeNode(vals[0])  # Create the root node using the first value.
        q = collections.deque([root])  # Initialize the queue with the root node.

        # Iterate through the list of node values two at a time (left and right children).
        for i in range(1, len(vals), 2):
            node = q.popleft()  # Dequeue the parent node.
            if vals[i] != 'n':  # Check if the left child exists.
                node.left = TreeNode(vals[i])  # Create the left child node.
                q.append(node.left)  # Enqueue the left child.
            if i + 1 < len(vals) and vals[i + 1] != 'n':  # Check if the right child exists.
                node.right = TreeNode(vals[i + 1])  # Create the right child node.
                q.append(node.right)  # Enqueue the right child.

        return root  # Return the root of the reconstructed binary tree.
