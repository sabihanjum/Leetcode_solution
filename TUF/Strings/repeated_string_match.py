"""Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc"."""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = math.ceil(len(b) / len(a))
        s = a * n
        if b in s:
            return n
        if b in s + a:
            return n + 1
        return -1