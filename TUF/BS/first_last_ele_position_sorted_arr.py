"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to perform binary search.
        # If 'is_searching_left' is True, it searches for the leftmost occurrence of 'target'.
        # Otherwise, it searches for the rightmost occurrence.
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1  # Initialize index to -1 (in case the target is not found)

            while left <= right:
                mid = (left + right) // 2  # Calculate mid-point

                if nums[mid] > target:
                    # If mid element is greater than target, search the left half
                    right = mid - 1
                elif nums[mid] < target:
                    # If mid element is smaller than target, search the right half
                    left = mid + 1
                else:
                    # If target is found, record the index
                    idx = mid
                    if is_searching_left:
                        # If we're searching for the leftmost occurrence, continue to the left
                        right = mid - 1
                    else:
                        # If we're searching for the rightmost occurrence, continue to the right
                        left = mid + 1  # Corrected: We move right to find the rightmost occurrence
            return idx

        # Perform binary search to find the leftmost index of the target
        left = binary_search(nums, target, True)

        # Perform binary search to find the rightmost index of the target
        right = binary_search(nums, target, False)

        return [left, right]  # Return the positions of the leftmost and rightmost occurrences
