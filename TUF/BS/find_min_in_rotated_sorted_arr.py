"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time."""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # N is the length of the array
        N = len(nums)
        # Initialize left and right pointers
        l, r = 0, N - 1

        # Loop continues until the left and right pointers converge
        while l < r:
            # Calculate the middle index
            mid = (l + r) // 2
            
            # If the middle element is greater than the right element, 
            # this means the smallest element is in the right half
            if nums[mid] > nums[r]:
                l = mid + 1  # Move the left pointer to mid + 1
            else:
                # If the middle element is smaller than or equal to the right element,
                # this means the smallest element is in the left half (or at mid)
                r = mid  # Narrow down the right pointer to mid

        # When the loop ends, l will point to the minimum element
        return nums[l]
