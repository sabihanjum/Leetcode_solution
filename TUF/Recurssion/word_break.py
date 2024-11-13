"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation."""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a DP array where dp[i] is True if s[i:] can be segmented into words from the dictionary
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty substring can always be segmented
        
        # Iterate over the string `s` from the end towards the start
        for i in range(len(s) - 1, -1, -1):
            # Check each word in the dictionary to see if it matches the substring starting at i
            for w in wordDict:
                # Check if the word `w` fits in the remaining substring and matches `s[i:i+len(w)]`
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Set dp[i] based on whether the remainder of the string can be segmented
                if dp[i]:  # If we found a valid segmentation, no need to check further words
                    break
        
        # Return dp[0], which represents whether the entire string `s` can be segmented
        return dp[0]
