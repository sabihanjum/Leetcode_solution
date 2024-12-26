"""Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string ""."""

class Solution:
    def checkValidString(self, s: str) -> bool:
        # `leftMin` tracks the minimum possible open parentheses count
        # `leftMax` tracks the maximum possible open parentheses count
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(": 
                # If the character is '(', it increases the count of open parentheses
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")": 
                # If the character is ')', it decreases the count of open parentheses
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else: 
                # If the character is '*', it can act as '(', ')' or an empty string
                # Hence, decrease the minimum and increase the maximum open count
                leftMin, leftMax = leftMin - 1, leftMax + 1

            # If `leftMax` becomes negative, there are too many ')' making the string invalid
            if leftMax < 0:
                return False

            # Ensure `leftMin` is never negative (minimum count cannot go below 0)
            # This accounts for situations where '*' balances out unmatched ')'
            if leftMin < 0:
                leftMin = 0

        # Finally, if `leftMin` is 0, it means the string can be valid
        return leftMin == 0
