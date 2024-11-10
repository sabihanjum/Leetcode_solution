"""Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the
combinations may be returned in any order."""



from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []  # Initialize an empty list to store valid combinations

        # Helper function for backtracking
        def backtrack(num, stack, target):
            # Base case: if we have exactly k numbers in the stack
            if len(stack) == k:
                # Check if the sum of the numbers in stack equals the target
                if target == 0:
                    res.append(stack)  # Add a valid combination to the result
                return  # Backtrack if stack length is k, regardless of target
            
            # Try each number from num+1 to 9
            for x in range(num + 1, 10):
                # Only proceed if the current number x is less than or equal to target
                if x <= target:
                    # Recurse with the updated stack and reduced target
                    backtrack(x, stack + [x], target - x)
                else:
                    # Early exit if x is greater than the remaining target, no need to check further
                    return

        # Start backtracking from 1 with an empty stack and the initial target n
        backtrack(0, [], n)
        return res  # Return all valid combinations found
