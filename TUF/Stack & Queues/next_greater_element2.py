"""Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Length of the input array
        n = len(nums)
        
        # Initialize the result array with -1, as default value for no next greater element
        ans = [-1] * n
        
        # Stack to store indices of elements in the array
        stack = []
        
        # First pass: Iterate through the array to find next greater elements
        for i in range(n):
            # While stack is not empty and the current element is greater than
            # the element at the index stored on top of the stack:
            while stack and nums[i] > nums[stack[-1]]:
                # Pop the index from the stack and assign the current element as its next greater element
                ans[stack.pop()] = nums[i]
            # Push the current index onto the stack
            stack.append(i)
        
        # Second pass: Handle circular nature of the array
        # Iterate through the array again to find next greater elements for elements left in the stack
        for i in range(n):
            # If we reach the index at the top of the stack, it means we've cycled through the array
            if i == stack[-1]:
                break
            # While stack is not empty and the current element is greater than
            # the element at the index stored on top of the stack:
            while stack and nums[i] > nums[stack[-1]]:
                # Pop the index from the stack and assign the current element as its next greater element
                ans[stack.pop()] = nums[i]
        
        # Return the result array with the next greater elements
        return ans
