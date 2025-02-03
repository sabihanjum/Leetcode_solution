"""Given two strings text and pattern, find the first index where pattern exactly matches with any substring of text. 

Return -1 if pattern doesn't exist as a substring in text."""
class Solution:
    def findMatching(self, text, pattern):
        # Code here
        m=len(pattern)
        for i in range(len(text)):
            if pattern==text[i:i+m]:
                return i
        return -1