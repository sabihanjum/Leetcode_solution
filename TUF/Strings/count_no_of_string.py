
"""Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters. 

Example 1:

Input: S = "aba", K = 2
Output:3
Explanation:The substrings are: "ab", "ba" and "aba"."""

class Solution:
    
    # Helper function to count substrings with exactly 'k' distinct characters
    def substrk(self, s, l, k):
        
        # Initialize variables
        f = 0  # A flag (unused in the current logic but declared)
        dct = {}  # Dictionary to keep track of character frequencies in the current window
        i, j = 0, 0  # i and j are pointers to mark the window's boundaries
        cnt = 0  # Count of substrings with exactly 'k' distinct characters
        
        # Iterate through the string with the 'i' pointer
        for i in range(0, l):
            
            # Expand the window with the 'j' pointer until it contains 'k' distinct characters
            while j < l and len(dct) < k:
                if s[j] not in dct:
                    # If the character at 'j' is not in the dictionary, add it with count 1
                    dct[s[j]] = 1
                else:
                    # Otherwise, increase the count of that character
                    dct[s[j]] += 1
                
                j += 1
            
            # If the window contains 'k' or more distinct characters, add the number of valid substrings
            if len(dct) >= k:
                cnt += l - j + 1  # All substrings from the current 'i' to 'j' are valid
            
            # Shrink the window from the left side by reducing the frequency of character 's[i]'
            dct[s[i]] -= 1
            if dct[s[i]] == 0:
                # If the count of the character 's[i]' reaches zero, remove it from the dictionary
                del dct[s[i]]
        
        # Return the count of valid substrings
        return cnt
            
    # Main function to count substrings with exactly 'k' distinct characters
    def substrCount(self, s, k):
        l = len(s)  # Get the length of the string
        
        # Count substrings with exactly 'k' distinct characters by subtracting
        # the count of substrings with exactly 'k+1' distinct characters
        return self.substrk(s, l, k) - self.substrk(s, l, k+1)
