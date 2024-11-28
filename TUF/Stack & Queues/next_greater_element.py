"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above."""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to store the next greater element for each number in nums2
        ans = {}
        
        # Result list to store the next greater elements for nums1
        res = []
        
        # Stack to help find the next greater element
        stack = []
        
        # Iterate over each number in nums2
        for n2 in nums2:
            # While the stack is not empty and the current number is greater than
            # the top of the stack, the current number is the next greater element
            # for the top of the stack.
            while stack and n2 > stack[-1]:
                ans[stack.pop()] = n2  # Pop the stack and map the popped element to n2
            
            # Push the current number onto the stack for further comparison
            stack.append(n2)
        
        # After processing nums2, for numbers left in the stack, no next greater element exists
        # These are handled implicitly by the dictionary (not assigned, so return -1 by default).
        
        # For each number in nums1, fetch the next greater element from the dictionary.
        # If the number is not in the dictionary, return -1 as the default value.
        for n1 in nums1:
            res.append(ans.get(n1, -1))
        
        # Return the result list
        return res
