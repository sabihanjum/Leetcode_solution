class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Initialize an empty string to store the result
        res = ""
        
        # Initialize counters for open and close parentheses
        open = 0
        close = 0
        
        # Variable to track the start index of a primitive group of parentheses
        start = 0

        # Iterate through the string 's' character by character
        for i in range(0, len(s)):
            # If the current character is an open parenthesis '(', increment the open counter
            if s[i] == '(':
                open += 1
            # If the current character is a close parenthesis ')', increment the close counter
            elif s[i] == ')':
                close += 1

            # When the number of open and close parentheses are equal, we have found a valid primitive group
            if open == close:
                # Append the part of the string between the outermost parentheses to the result
                res = res + s[start + 1:i]
                
                # Update the start index for the next primitive group
                start = i + 1
                
                # Reset the open and close counters for the next group
                open = 0
                close = 0

        # Return the result string, which contains the input string with the outermost parentheses removed
        return res
