"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search loop continues until the pointers cross
        while l <= r:
            # Find the middle index
            mid = (l + r) // 2

            # Check if the middle element is the target
            if target == nums[mid]:
                return mid  # Target found, return the index

            # Check if the left side of the array is sorted
            if nums[l] <= nums[mid]:
                # If target is outside the sorted left side range, search right
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # Move left pointer to mid + 1
                else:
                    r = mid - 1  # Search in the sorted left side
            else:
                # Otherwise, the right side is sorted
                # If target is outside the sorted right side range, search left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # Move right pointer to mid - 1
                else:
                    l = mid + 1  # Search in the sorted right side

        # Return -1 if the target is not found in the array
        return -1
