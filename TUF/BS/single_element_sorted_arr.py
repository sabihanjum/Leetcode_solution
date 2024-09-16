"""You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space."""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Initialize the pointers for binary search
        l = 0
        r = len(nums) - 1

        # Perform binary search to find the single non-duplicate element
        while l < r:
            # Calculate the middle index
            m = (l + r) // 2
            
            # Ensure 'm' is even (for comparison with the next element)
            if m % 2 == 1:
                m -= 1
            
            # If the element at 'm' is equal to the element at 'm + 1'
            if nums[m] == nums[m + 1]:
                # Move to the right half of the array
                l = m + 2
            else:
                # Move to the left half of the array
                r = m

        # When the loop ends, 'l' will point to the index of the single non-duplicate element
        return nums[l]