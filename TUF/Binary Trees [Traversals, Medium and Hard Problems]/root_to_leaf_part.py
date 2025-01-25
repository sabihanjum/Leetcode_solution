"""Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree."""

from typing import Optional
from collections import deque

from typing import List

class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        """
        Function to find all paths from root to leaf in a binary tree.
        
        Args:
        root: The root node of the binary tree.
        
        Returns:
        A list of lists, where each list represents a path from root to leaf.
        """
        # Initialize a list to store all the paths.
        self.ans = []
        
        # Initialize a list to keep track of the current path.
        self.path = []
        
        # Call the helper function to populate `self.ans`.
        self.helper(root)
        
        # Return all the collected paths.
        return self.ans

    def helper(self, root):
        """
        Helper function to recursively traverse the binary tree and construct paths.
        
        Args:
        root: The current node being processed.
        """
        if not root:
            # If the current node is None, there's nothing to process, so return.
            return
        
        # Add the current node's data to the path.
        self.path.append(root.data)
        
        # If the current node is a leaf node (no left or right child):
        if not root.left and not root.right:
            # Create a duplicate of the current path to prevent mutation issues.
            duplicate = [x for x in self.path]
            
            # Add the duplicate path to the result list.
            self.ans.append(duplicate)
            
            # Remove the current node from the path and backtrack.
            return self.path.pop()
        
        # Recursively process the left and right children.
        self.helper(root.left)
        self.helper(root.right)
        
        # Remove the current node from the path after processing its children (backtracking).
        return self.path.pop()
