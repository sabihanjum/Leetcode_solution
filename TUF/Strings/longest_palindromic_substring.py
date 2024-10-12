"""Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer."""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize the result string and its length
        res = ""
        resLen = 0

        # Loop through each character in the string as a potential center of a palindrome
        for i in range(len(s)):
            # Check for odd-length palindromes with center at s[i]
            l, r = i, i  # Start with both pointers at the same position
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand while characters on both sides are equal
                if (r - l + 1) >= resLen:  # If the current palindrome is longer or equal to the previous one
                    res = s[l:r+1]  # Update the result with the new palindrome
                    resLen = r - l + 1  # Update the maximum length
                l -= 1  # Move the left pointer outwards
                r += 1  # Move the right pointer outwards

            # Check for even-length palindromes with centers at s[i] and s[i+1]
            l, r = i, i + 1  # Start with pointers at consecutive positions
            while l >= 0 and r < len(s) and s[l] == s[r]:  # Expand while characters on both sides are equal
                if (r - l + 1) >= resLen:  # If the current palindrome is longer or equal to the previous one
                    res = s[l:r+1]  # Update the result with the new palindrome
                    resLen = r - l + 1  # Update the maximum length
                l -= 1  # Move the left pointer outwards
                r += 1  # Move the right pointer outwards

        # Return the longest palindrome found
        return res
