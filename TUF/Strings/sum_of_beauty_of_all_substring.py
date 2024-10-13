"""The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.
Example 1:
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1."""

import collections

class Solution:
    def beautySum(self, s: str) -> int:
        # Initialize the total beauty sum to 0
        ans = 0
        
        # Outer loop to set the starting index of the substring
        for i in range(len(s)):
            # Use a counter to store the frequency of characters in the current substring
            count = collections.Counter()
            
            # Inner loop to extend the substring and calculate its beauty
            for j in range(i, len(s)):
                # Increment the count of the current character in the substring
                count[s[j]] += 1
                
                # Calculate the beauty of the current substring
                # Beauty is defined as the difference between the maximum and minimum frequency of characters
                ans += max(count.values()) - min(count.values())
        
        # Return the total beauty sum of all substrings
        return ans
