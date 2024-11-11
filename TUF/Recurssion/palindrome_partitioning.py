"""Given a string s, partition s such that every substring of the partition is a palindrome.Return all possible 
palindrome partitioning of s."""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # This will store all the possible palindrome partitions
        part = []  # This will store the current partition being built

        # Depth-First Search helper function
        def dfs(i):
            # If we've reached the end of the string, add the current partition to results
            if i >= len(s):
                res.append(part.copy())  # Append a copy of the current partition
                return
            
            # Try to partition the string from index i to the end
            for j in range(i, len(s)):
                # If the substring s[i:j+1] is a palindrome, proceed with this partition
                if isPali(s, i, j):
                    part.append(s[i:j+1])  # Add the palindrome substring to the current partition
                    dfs(j + 1)  # Recurse with the next index
                    part.pop()  # Backtrack by removing the last added substring

        # Helper function to check if a substring s[l:r+1] is a palindrome
        def isPali(s, l, r):
            # Check if the substring is the same forwards and backwards
            while l < r:
                if s[l] != s[r]:  # If characters at l and r don't match, it's not a palindrome
                    return False
                l += 1
                r -= 1
            return True  # The substring is a palindrome

        dfs(0)  # Start the DFS with the initial index 0
        return res  # Return all the palindrome partitions found
