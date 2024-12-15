"""Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique."""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Counter to keep track of characters needed from t
        c = Counter(t)
        # Overall count of distinct characters needed from t
        overall = len(c)

        r = 0  # Right pointer for the sliding window
        l = 0  # Left pointer for the sliding window
        res = ""  # To store the result substring

        while r < len(s):
            # Expand the window to include s[r]
            if s[r] in c:
                c[s[r]] -= 1
                if c[s[r]] == 0:
                    overall -= 1

            # Contract the window from the left while all required characters are present
            while overall == 0:
                # Update the result if this is the smallest window found so far
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]

                # Shrink the window from the left
                if s[l] in c:
                    c[s[l]] += 1
                    if c[s[l]] > 0:
                        overall += 1
                l += 1

            r += 1

        return res
