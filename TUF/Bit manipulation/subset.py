"""Given an integer array nums of unique elements, return all possible 
subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, subset: List[int]):
            # Add a copy of the current subset to the result
            res.append(subset[:])
            
            # Iterate over the range starting from 'start' to the end of the list
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                subset.append(nums[i])
                # Recursively call backtrack with the next index
                backtrack(i + 1, subset)
                # Backtrack by removing the last element
                subset.pop()
        
        res = []
        backtrack(0, [])
        return res