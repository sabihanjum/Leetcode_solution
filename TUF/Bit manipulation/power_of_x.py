"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn)."""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implements the power function (x^n) recursively.
        
        Parameters:
        x (float): The base number.
        n (int): The exponent.
        
        Returns:
        float: The result of x raised to the power of n.
        """
        # Base case: Any number raised to the power of 0 is 1
        if n == 0:
            return 1
        
        # If the exponent is negative, invert the base and make the exponent positive
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # If the exponent is odd, multiply the base with the result of (x^(n-1))
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        
        # If the exponent is even, compute (x^(n//2)) and square it
        return self.myPow(x * x, n // 2)
