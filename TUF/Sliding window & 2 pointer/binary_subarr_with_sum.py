"""Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array."""
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        ans = 0
        prefix = 0
        # Initialize a dictionary to store the frequency of prefix sums.
        # Start with {0: 1} since a prefix sum of 0 can be achieved before processing any element.
        count = Counter({0: 1})

        # Iterate through each number in the array
        for num in nums:
            # Update the prefix sum
            prefix += num
            # Check if (prefix - goal) exists in the count dictionary.
            # If it exists, it means there are subarrays ending at the current index
            # whose sum equals the goal. Add the frequency to the answer.
            ans += count[prefix - goal]
            # Increment the count of the current prefix sum in the dictionary
            count[prefix] += 1

        # Return the total number of subarrays with the specified sum
        return ans

