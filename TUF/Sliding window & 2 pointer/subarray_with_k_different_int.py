"""Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array."""

import collections

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Helper function to count subarrays with at most k distinct numbers
        def subarraysWithAtMostKDistinct(k: int) -> int:
            res = 0
            count = collections.Counter()

            l = 0
            # Traverse the array with the right pointer 'r'
            for r, num in enumerate(nums):
                count[num] += 1
                # If adding this number makes the count of distinct numbers greater than 'k',
                # move the left pointer 'l' until the condition is met
                if count[num] == 1:
                    k -= 1
                while k < 0:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        k += 1
                    l += 1
                # The number of subarrays ending at 'r' with at most 'k' distinct numbers
                res += r - l + 1

            return res

        # Calculate subarrays with exactly 'k' distinct numbers by subtracting
        # subarrays with at most 'k-1' distinct numbers from those with at most 'k' distinct numbers
        return subarraysWithAtMostKDistinct(k) - subarraysWithAtMostKDistinct(k - 1)
