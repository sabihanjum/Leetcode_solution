"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to handle duplicates and to simplify the process of finding combinations
        candidates.sort()

        res = []
        
        # Define the backtracking function to explore combinations
        def backtrack(cur, pos, target):
            # Base case: if the target is zero, we've found a valid combination
            if target == 0:
                res.append(cur.copy())  # Add a copy of the current combination to the result
                return
            # If the target is less than zero, stop exploring this path
            if target < 0:
                return
            
            prev = -1  # Initialize a variable to keep track of the previous candidate at each position
            for i in range(pos, len(candidates)):
                # Skip duplicates by checking if the current candidate equals the previous one
                if candidates[i] == prev:
                    continue

                # Include candidates[i] in the current combination and proceed recursively
                cur.append(candidates[i])
                # Move to the next position (i+1) and reduce the target by candidates[i]
                backtrack(cur, i + 1, target - candidates[i])
                # Backtrack: remove the last added element to explore other combinations
                cur.pop()

                # Update prev to the current candidate to avoid duplicates in the next iteration
                prev = candidates[i]

        # Start backtracking with an empty combination list, starting at position 0, and with the given target
        backtrack([], 0, target)
        return res

# Example usage:
# solution = Solution()
# print(solution.combinationSum2([10,1,2,7,6,1,5], 8)) 
# Expected output: [[1,1,6], [1,2,5], [1,7], [2,6]]
