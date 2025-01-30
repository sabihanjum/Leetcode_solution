"""Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise."""

from typing import Optional
from collections import defaultdict

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = set()  # Use a set to store values

        def dfs(node):
            if not node:
                return False  # Base case: if node is None, return False
            
            y = k - node.val  # Compute the complement value
            if y in l:
                return True  # If complement is found, return True
            
            l.add(node.val)  # Add current node value to set
            
            # Recursively search left and right subtrees
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
