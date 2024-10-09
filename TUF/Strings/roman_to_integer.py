"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3."""


class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a lookup dictionary that maps Roman numerals to their corresponding integer values
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Get the length of the string
        N = len(s)
        # Start from the last character of the string
        i = N - 1
        # Initialize output to store the result of conversion
        output = 0

        # Traverse the string from the end to the beginning
        while i >= 0:
            # If the current Roman numeral is less than the next one, we subtract it
            # This handles cases like IV (4) or IX (9) where smaller numerals precede larger ones
            if i < N - 1 and lookup[s[i]] < lookup[s[i+1]]:
                output -= lookup[s[i]]
            # Otherwise, we add the value to the output
            else:
                output += lookup[s[i]]
            # Move to the previous character
            i -= 1
        
        # Return the final integer value
        return output
