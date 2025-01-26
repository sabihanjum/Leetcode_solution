"""Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST."""
class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        
        curr = root
        while curr.left is not None:
            curr = curr.left
        return curr.data