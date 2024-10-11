"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result."""

class Solution:
    def myAtoi(self, s: str) -> int:
        # If the input string is empty, return 0
        if not s:
            return 0
        
        n = len(s)
        if n == 0:
            return 0
        
        i = 0
        # Skip any leading spaces
        while i < n and s[i] == ' ':
            i += 1
            
            # If we reach the end after skipping spaces, return 0
            if i == n:
                return 0
        
        # Determine the sign of the number: -1 for negative, 1 for positive
        sign = -1 if s[i] == '-' else 1
        
        # Move the pointer past the sign if it's '+' or '-'
        if s[i] in ['-', '+']:
            i += 1
        
        # Initialize the result variable and a flag to prevent overflow
        res, flag = 0, (2**31 - 1) // 10
        
        # Loop through the string as long as there are digits
        while i < n:
            # If the current character is not a digit, break out of the loop
            if not s[i].isdigit():
                break
            
            # Convert the current character to an integer
            c = int(s[i])
            
            # Check for overflow conditions
            if res > flag or (res == flag and c > 7):
                # Return INT_MAX (2**31 - 1) if positive or INT_MIN (-2**31) if negative
                return 2**31 - 1 if sign > 0 else -(2**31)
            
            # Accumulate the result by multiplying by 10 and adding the current digit
            res = res * 10 + c
            i += 1
        
        # Return the final result, taking into account the sign
        return sign * res
