class Solution:
    def reverse(self, x: int) -> int:
        revNum = 0  # Initialize the variable to store the reversed number
        is_negative = x < 0  # Check if the number is negative
        x = abs(x)  # Take the absolute value of x to handle negative numbers
        
        while x != 0:
            ld = x % 10  # Get the last digit of x
            revNum = revNum * 10 + ld  # Add the last digit to the reversed number
            x //= 10  # Remove the last digit from x by integer division
        
        # Check for 32-bit integer overflow
        if revNum > 2**31 - 1:  
            return 0  # Return 0 if the reversed number exceeds 32-bit integer limit
        
        # If the original number was negative, make the reversed number negative
        return -revNum if is_negative else revNum
