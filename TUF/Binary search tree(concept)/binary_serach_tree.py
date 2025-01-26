"""Given an array of integers arr[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.

Note - In a valid Binary Search Tree all keys are unique."""

class Solution:
    def isBSTTraversal(self, nums):
        
        # Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is less than or equal to the previous one
            if nums[i-1] >= nums[i]:
                # If a violation of the BST property is found, return False
                return False
                
        # If the loop completes without finding violations, the sequence is valid
        return True
