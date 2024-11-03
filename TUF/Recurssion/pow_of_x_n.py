"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn)."""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: any number to the power of 0 is 1
        if n == 0:
            return 1
        
        # If the power is negative, invert x and make n positive
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # If n is odd, multiply x once and reduce the power by 1 to make it even
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        
        # If n is even, use exponentiation by squaring to optimize
        return self.myPow(x * x, n // 2)
