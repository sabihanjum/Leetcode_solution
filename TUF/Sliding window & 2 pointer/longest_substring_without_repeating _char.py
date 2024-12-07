"""Given a string s, find the length of the longest substring without repeating characters."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A set to store the unique characters in the current window
        charSet = set()
        
        # Initialize the left pointer of the window and the result variable
        l = 0
        res = 0
        
        # Iterate through the string with the right pointer
        for r in range(len(s)):
            # If the current character is already in the set (duplicate found)
            while s[r] in charSet:
                # Remove the character at the left pointer from the set
                charSet.remove(s[l])
                # Move the left pointer to the right, shrinking the window
                l += 1
            
            # Add the current character to the set
            charSet.add(s[r])
            
            # Update the result with the maximum length of the substring
            # calculated as the difference between right and left pointers + 1
            res = max(res, r - l + 1)
        
        # Return the length of the longest substring without repeating characters
        return res
