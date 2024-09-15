"""There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible."""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initialize two pointers for binary search
        l, r = 0, len(nums) - 1
        
        # Perform binary search while the left pointer is less than or equal to the right
        while l <= r:
            # Calculate the middle index
            m = l + (r - l) // 2  # Use (r - l) instead of (r - 1) for correct mid calculation

            # If the middle element is the target, return True
            if nums[m] == target:
                return True

            # If the left half is sorted
            if nums[l] < nums[m]:
                # Check if the target lies within the sorted left half
                if nums[l] <= target < nums[m]:
                    # Narrow the search to the left half
                    r = m - 1
                else:
                    # Narrow the search to the right half
                    l = m + 1
            
            # If the right half is sorted
            elif nums[l] > nums[m]:
                # Check if the target lies within the sorted right half
                if nums[m] < target <= nums[r]:
                    # Narrow the search to the right half
                    l = m + 1
                else:
                    # Narrow the search to the left half
                    r = m - 1
            
            # If the leftmost and mid element are the same, we can't decide which half is sorted
            else:
                # Increment the left pointer to skip duplicates
                l += 1

        # If the target is not found, return False
        return False
