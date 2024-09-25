"""Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array."""


from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1  # Start with one subarray
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1  # We need a new subarray
                    currSum = n  # Start the new subarray with the current number
            return subarray <= k  # Check if we can split into k or fewer subarrays

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
