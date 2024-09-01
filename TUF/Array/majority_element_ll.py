from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)  # Dictionary to keep track of candidate elements and their counts

        # First pass: Find potential candidates for the majority element
        for n in nums:
            count[n] += 1  # Increment the count for the current element

            # If there are more than two candidates, reduce their counts
            if len(count) > 2:
                new_count = defaultdict(int)  # Initialize a new count dictionary
                for key, c in count.items():
                    if c > 1:  # Only retain elements with count > 1
                        new_count[key] = c - 1  # Decrease their count by 1
                count = new_count  # Update the count dictionary with reduced counts

        # Second pass: Validate the candidates
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:  # Check if candidate appears more than n/3 times
                res.append(n)

        return res  # Return the list of valid majority elements
