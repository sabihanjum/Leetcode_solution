"""Given a list arr of n integers, return sums of all subsets in it. Output sums can be printed in any order."""

class Solution:
    def subsetSums(self, arr, n):
        ans = []  # Initialize an empty list to store all subset sums
        
        # Helper function to recursively calculate subset sums
        def subset(l, r, current_sum, arr):
            # Base case: if the left index exceeds the right, add current_sum to results
            if l > r:
                ans.append(current_sum)
                return
            
            # Include the current element in the subset and move to the next element
            subset(l + 1, r, current_sum + arr[l], arr)
            
            # Exclude the current element from the subset and move to the next element
            subset(l + 1, r, current_sum, arr)
        
        # Start the recursive process from the first index with an initial sum of 0
        subset(0, n - 1, 0, arr)
        
        # Sort the result to have subset sums in ascending order
        ans.sort()
        return ans  # Return the list of all possible subset sums
