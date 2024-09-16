"""A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time."""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize the left and right pointers for binary search
        l, r = 0, len(nums) - 1

        # Perform binary search to find a peak element
        while l <= r:
            # Calculate the middle index
            m = l + ((r - l) // 2)
            
            # Check if the middle element is less than its left neighbor
            if m > 0 and nums[m] < nums[m - 1]:
                # If so, move the search to the left half of the array
                r = m - 1
            # Check if the middle element is less than its right neighbor
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                # If so, move the search to the right half of the array
                l = m + 1
            else:
                # If neither condition is true, we have found a peak element
                return m
