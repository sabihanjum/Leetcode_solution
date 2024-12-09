"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations."""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0               # Variable to store the maximum length of substring
        maxCount = 0          # Variable to keep track of the maximum frequency of any character in the current window
        count = Counter()     # Counter to keep track of character frequencies within the current window

        l = 0  # Left pointer for the window
        for r, c in enumerate(s):
            count[c] += 1                 # Increment the count of the current character
            maxCount = max(maxCount, count[c]) # Update maxCount with the highest character frequency in the current window

        # While the size of the window minus the frequency of the most common character is greater than k,
        # we shrink the window from the left until the condition is met
        while maxCount + k < r - l + 1:
            count[s[l]] -= 1
            l += 1

        ans = max(ans, r - l + 1)      # Update the answer with the maximum length of valid substring found

        return ans
