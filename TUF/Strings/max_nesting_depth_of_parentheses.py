"""Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3"""

class Solution:
    def maxDepth(self, s: str) -> int:
        # Initialize count to track the current depth of nested parentheses
        count = 0
        # Initialize max_num to track the maximum depth encountered
        max_num = 0
        
        # Loop through each character in the string
        for i in s:
            # If an opening parenthesis is encountered, increase the depth (count)
            if i == "(":
                count += 1
                # Update max_num if the current depth exceeds the recorded maximum depth
                if max_num < count:
                    max_num = count
            # If a closing parenthesis is encountered, decrease the depth (count)
            if i == ")":
                count -= 1
        
        # Return the maximum depth of nested parentheses
        return(max_num)
