"""Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays."""

from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize counter for odd counts with 0 count as 1 (base case)
        odd_count = Counter({0: 1})
        # Initialize variables for the answer and the temporary count of odds
        answer = temp_odd_count = 0
        # Iterate over each value in the list
        for value in nums:
            # Increment temp_odd_count if value is odd
            temp_odd_count += value & 1  # value & 1 is 1 if value is odd, 0 otherwise
            # If there are at least k odd numbers, add the count to answer
            # This checks if a valid subarray ending at the current index exists
            answer += odd_count[temp_odd_count - k]
            # Increment the count of the current number of odd integers seen so far
            odd_count[temp_odd_count] += 1
        # Return the total number of valid subarrays
        return answer

