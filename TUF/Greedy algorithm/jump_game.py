"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Initialize two variables:
        # `i` is the current index we are checking.
        # `reach` keeps track of the farthest index we can reach so far.
        i = 0
        reach = 0

        # Loop through the array while `i` is within the bounds of the array
        # and is reachable (i.e., `i <= reach`).
        while i < len(nums) and i <= reach:
            # Update `reach` to the maximum of its current value
            # or the farthest index we can jump to from the current index (`i + nums[i]`).
            reach = max(reach, i + nums[i])
            # Move to the next index.
            i += 1

        # If `i` equals the length of the array, it means we were able to reach or pass
        # the last index. Otherwise, return `False`.
        return i == len(nums)
