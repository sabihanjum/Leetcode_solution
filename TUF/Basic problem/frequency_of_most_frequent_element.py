"""The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an
 index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations."""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array to make it easier to calculate the frequency of the largest value
        nums.sort()
        
        # Initialize pointers for the sliding window (l for left, r for right)
        l, r = 0, 0
        
        # Initialize variables to store the maximum frequency found (res) and the sum of the current window (total)
        res, total = 0, 0

        # Iterate through the array with the right pointer (r)
        while r < len(nums):
            # Add the current number to the total sum of the window
            total += nums[r]
            
            # Check if the current window can be adjusted to have all elements equal to nums[r]
            # If nums[r] multiplied by the number of elements in the window (r - l + 1) exceeds
            # the total sum plus k, then we can't make all elements equal to nums[r] with at most k operations
            while nums[r] * (r - l + 1) > total + k:
                # If the window is invalid, reduce its size from the left
                total -= nums[l]
                l += 1

            # Update the result with the maximum frequency found
            res = max(res, r - l + 1)
            
            # Move the right pointer to expand the window
            r += 1
        
        # Return the maximum frequency found
        return res
