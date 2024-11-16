"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is less than or equal to 0
        if n <= 0:
            return False
    
        # Check if n has only one bit set to 1
        return n & (n - 1) == 0