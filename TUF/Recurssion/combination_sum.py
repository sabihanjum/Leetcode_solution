"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input."""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize a list of empty lists where dp[i] will store all unique combinations that sum up to 'i'
        dp = [[] for _ in range(target + 1)]

        # Iterate through each candidate number
        for c in candidates:
            # For each candidate, iterate over all target values from 1 up to the given target
            for i in range(1, target + 1):
                # If the current target 'i' is less than the candidate 'c', skip it as 'c' can't contribute
                if i < c:
                    continue
                # If the target 'i' is exactly equal to the candidate 'c', then add [c] as a valid combination
                if i == c:
                    dp[i].append([c])
                else:
                    # If 'i' is greater than 'c', look at dp[i - c] (combinations that sum up to 'i - c')
                    # For each combination that can make 'i - c', add 'c' to it to form a new combination
                    for blist in dp[i - c]:
                        dp[i].append(blist + [c])

        # dp[target] now contains all combinations that sum up to the target
        return dp[target]