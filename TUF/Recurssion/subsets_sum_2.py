"""Given an integer array nums that may contain duplicates, return all possible subsets(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order."""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Helper function for Depth-First Search (DFS) to generate subsets
        def dfs(start_index, path):
            # Add the current path (subset) to the answer list
            ans.append(path[:])  # Make a copy of the path to avoid reference issues
            
            # Iterate over the elements starting from start_index to form subsets
            for i in range(start_index, len(nums)):
                # Skip duplicates - if the current element is the same as the previous element
                # and we're not at the start of this recursive level, continue to avoid duplicates
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the current subset path
                path.append(nums[i])
                
                # Recurse to continue building the subset from the next index
                dfs(i + 1, path)
                
                # Backtrack by removing the last element, preparing for the next iteration
                path.pop()
        
        ans = []  # Initialize a list to store all unique subsets
        nums.sort()  # Sort the input list to handle duplicates easily
        dfs(0, [])  # Start the DFS from index 0 with an empty path
        return ans  # Return the list of all unique subsets
