"""Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for the 32-bit signed integer range
        INT_MAX = 2147483647  # Maximum allowed value
        INT_MIN = -2147483648  # Minimum allowed value

        # Handle edge case to prevent overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Take absolute values for calculation
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        # Perform the division using bit manipulation
        while d >= dv:
            temp = dv
            mul = 1
            # Double the divisor (temp) and multiplier (mul) until it's less than or equal to the dividend (d)
            while d >= temp:
                d -= temp  # Subtract the current divisor value from the dividend
                output += mul  # Add the corresponding multiplier to the result
                mul += mul  # Double the multiplier
                temp += temp  # Double the divisor value

        # Determine the sign of the result based on the signs of the inputs
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            output = -output

        # Ensure the result is within the 32-bit signed integer range
        return min(INT_MAX, max(INT_MIN, output))
